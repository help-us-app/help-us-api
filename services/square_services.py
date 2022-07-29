import json
from datetime import datetime

from constants.constants import Constants
from constants.variables import Variables
from models.commands.authorize_with_square_command import AuthorizeWithSquareCommand
from models.commands.checkout_with_square_command import CheckoutWithSquareCommand
from models.commands.delete_link_square_command import DeleteLinkSquareCommand
from models.commands.list_locations_square_command import ListLocationsSquareCommand
from models.commands.retrieve_location_square_command import RetrieveLocationSquareCommand
from models.commands.retrieve_with_square_command import RetrieveWithSquareCommand
from models.commands.set_merchant_info_webhook_command import SetMerchantInfoWebHookCommand
from models.commands.update_with_square_command import UpdateWithSquareCommand
from models.merchant_info import MerchantInfo
from models.requests.checkout_request import CheckoutRequest
from models.requests.obtain_token_request import ObtainTokenRequest
from models.responses.checkout_response import CheckoutResponse
from models.responses.location_response import LocationResponse, Location
from models.responses.obtain_token_response import ObtainTokenResponse
from models.user import User
from repository.directus_repository import DirectusRepository


class SquareService:
    def __init__(self, request):
        self.request = request
        self.variables = Variables()
        self.constants = Constants()
        self.directus_repository = DirectusRepository(self.request)

    def get_access_token(self, user_id) -> str:

        user: User = self.directus_repository.get_user_by_id(user_id)

        expires_in = datetime.strptime(user.expires_in, '%Y-%m-%dT%H:%M:%SZ')

        now = datetime.utcnow()
        if now > expires_in:
            response = AuthorizeWithSquareCommand(self, {
                'grant_type': "refresh_token",
                'refresh_token': user.refresh_token
            }).execute()
            self.directus_repository.set_merchant_information_for_user(user_id, MerchantInfo({
                'access_token': response.access_token,
                'refresh_token': response.refresh_token,
                'expires_in': response.expires_at
            }))
            user.access_token = response.access_token

        return user.access_token

    def authorize_with_square(self, command: AuthorizeWithSquareCommand):
        obtain_token_request = ObtainTokenRequest({
            'short_lived': True,
            'grant_type': command.grant_type,
            'client_id': self.variables.client_id,
            'client_secret': self.variables.client_secret,
            'scopes': self.constants.token_scopes,
            'refresh_token': command.refresh_token,
            'code': command.code
        })
        request_json = json.dumps(obtain_token_request.to_dict())
        headers = {self.constants.content_type: self.constants.application_json}
        response = self.request.request(self.constants.post,
                                        self.variables.square_url + self.constants.obtain_token_endpoint,
                                        data=request_json,
                                        headers=headers)
        response.raise_for_status()
        response_json = json.loads(response.text)
        return ObtainTokenResponse(response_json)

    def checkout_with_square(self, command: CheckoutWithSquareCommand) -> CheckoutResponse:
        access_token = self.get_access_token(command.user_id)
        checkout_request = CheckoutRequest({
            "order": {
                "location_id": command.location_id,
                "line_items": command.line_items,
                "payment_note": command.payment_note,
                "pre_populated_data": {
                    "buyer_email": command.buyer_email,
                }},
            'source': self.constants.app_name,
        })
        request_json = json.dumps(checkout_request.to_dict())
        headers = {self.constants.content_type: self.constants.application_json,
                   "Authorization": "Bearer " + access_token}
        response = self.request.request(self.constants.post,
                                        self.variables.square_url + self.constants.version + self.constants.payment_link_endpoint,
                                        data=request_json,
                                        headers=headers)
        print(response.text)
        response.raise_for_status()
        response_json = json.loads(response.text)
        return CheckoutResponse(response_json)

    def get_payment_link(self, command: RetrieveWithSquareCommand) -> CheckoutResponse:
        access_token = self.get_access_token(command.user_id)
        headers = {self.constants.content_type: self.constants.application_json,
                   "Authorization": "Bearer " + access_token}
        response = self.request.request(self.constants.get,
                                        self.variables.square_url + self.constants.version + self.constants.payment_link_endpoint + command.id,
                                        headers=headers)
        response.raise_for_status()
        response_json = json.loads(response.text)
        return CheckoutResponse(response_json)

    def update_with_square(self, command: UpdateWithSquareCommand) -> bool:
        access_token = self.get_access_token(command.user_id)
        payment_link: CheckoutResponse = RetrieveWithSquareCommand(self, {
            'user_id': command.user_id,
            'id': command.id
        }).execute()
        if payment_link is None:
            raise Exception('Payment link not found')
        headers = {self.constants.content_type: self.constants.application_json,
                   "Authorization": "Bearer " + access_token, 'Square-Version': '2022-06-16'}

        request_body = {"payment_link": {
            "payment_note": command.payment_note,
            "version": payment_link.payment_link.version
        }}

        request_json = json.dumps(request_body)

        response = self.request.request(self.constants.put,
                                        self.variables.square_url + self.constants.version + self.constants.payment_link_endpoint + command.id,
                                        headers=headers, data=request_json)
        response.raise_for_status()
        return True

    def delete_link_square(self, command: DeleteLinkSquareCommand) -> bool:
        access_token = self.get_access_token(command.user_id)
        headers = {self.constants.content_type: self.constants.application_json,
                   'Authorization': 'Bearer ' + access_token}

        response = self.request.request(self.constants.delete,
                                        self.variables.square_url + self.constants.version + self.constants.payment_link_endpoint + command.id,
                                        headers=headers)

        response.raise_for_status()
        return True

    def get_square_auth_link(self, user_id) -> str:
        scopes = '+'.join(self.constants.token_scopes)
        return self.variables.square_url + self.constants.authorize_endpoint + '?client_id=' + self.variables.client_id + '&scope=' + scopes + '&state=' + user_id

    def set_merchant_information_for_user(self, command: SetMerchantInfoWebHookCommand):
        merchant_info: MerchantInfo = MerchantInfo({
            "authorization_code": command.authorization_code,
            "merchant_id": command.merchant_id,
            "access_token": command.access_token,
            "refresh_token": command.refresh_token,
            "expires_in": command.expires_in,
        })
        return self.directus_repository.set_merchant_information_for_user(command.user_id, merchant_info)

    def get_location_information(self, command: RetrieveLocationSquareCommand) -> LocationResponse:
        access_token = self.get_access_token(command.user_id)
        headers = {self.constants.content_type: self.constants.application_json,
                   "Authorization": "Bearer " + access_token}
        response = self.request.request(self.constants.get,
                                        self.variables.square_url + self.constants.version + self.constants.location_endpoint + command.location_id,
                                        headers=headers)
        response.raise_for_status()
        response_json = json.loads(response.text)
        return LocationResponse(response_json)

    def list_locations(self, command: ListLocationsSquareCommand) -> [Location]:

        access_token = self.get_access_token(command.user_id)

        headers = {self.constants.content_type: self.constants.application_json,
                   "Authorization": "Bearer " + access_token}
        response = self.request.request(self.constants.get,
                                        self.variables.square_url + self.constants.version + self.constants.location_endpoint,
                                        headers=headers)
        response.raise_for_status()
        response_json = json.loads(response.text)

        for location in response_json['locations']:
            yield Location(location)
