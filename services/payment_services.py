import json
from constants.constants import Constants
from constants.variables import Variables
from models.commands.authorize_with_square_command import AuthorizeWithSquareCommand
from models.commands.checkout_with_square_command import CheckoutWithSquareCommand
from models.commands.delete_link_square_command import DeleteLinkSquareCommand
from models.commands.retrieve_with_square_command import RetrieveWithSquareCommand
from models.commands.update_with_square_command import UpdateWithSquareCommand
from models.requests.checkout_request import CheckoutRequest
from models.requests.obtain_token_request import ObtainTokenRequest
from models.responses.checkout_response import CheckoutResponse
from models.responses.obtain_token_response import ObtainTokenResponse


class PaymentService:
    def __init__(self, request):
        self.request = request
        self.variables = Variables()
        self.constants = Constants()

    def get_access_token(self, command) -> str:
        if command.access_token == '':
            authorization_result = AuthorizeWithSquareCommand(self, {
                'grant_type': 'refresh_token',
                'refresh_token': command.refresh_token,
            }).execute()
            return authorization_result.access_token
        else:
            return command.access_token

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
        access_token = self.get_access_token(command)
        checkout_request = CheckoutRequest({
            "order": {
                "customer_id": command.customer_id,
                "location_id": command.location_id,
                "line_items": command.line_items,
                "payment_note": command.payment_note,
                "pre_populated_data": {
                    "buyer_email": command.buyer_email,
                    "buyer_phone_number": command.buyer_phone_number,
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
        response.raise_for_status()
        response_json = json.loads(response.text)
        return CheckoutResponse(response_json)

    def get_payment_link(self, command: RetrieveWithSquareCommand) -> CheckoutResponse:
        access_token = self.get_access_token(command)
        headers = {self.constants.content_type: self.constants.application_json,
                   "Authorization": "Bearer " + access_token}
        response = self.request.request(self.constants.get,
                                        self.variables.square_url + self.constants.version + self.constants.payment_link_endpoint + command.id,
                                        headers=headers)
        response.raise_for_status()
        response_json = json.loads(response.text)
        return CheckoutResponse(response_json)

    def update_with_square(self, command: UpdateWithSquareCommand) -> bool:
        access_token = self.get_access_token(command)
        payment_link: CheckoutResponse = RetrieveWithSquareCommand(self, {
            'access_token': access_token,
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
        print(response.text)
        response.raise_for_status()
        return True

    def delete_link_square(self, command: DeleteLinkSquareCommand) -> bool:
        access_token = self.get_access_token(command)
        headers = {self.constants.content_type: self.constants.application_json,
                   'Authorization': 'Bearer ' + access_token}

        response = self.request.request(self.constants.delete,
                                        self.variables.square_url + self.constants.version + self.constants.payment_link_endpoint + command.id,
                                        headers=headers)

        response.raise_for_status()
        return True
