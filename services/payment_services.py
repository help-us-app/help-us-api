import json
from constants.constants import Constants
from constants.variables import Variables
from models.commands.authorize_with_square_command import AuthorizeWithSquareCommand
from models.commands.checkout_with_square_command import CheckoutWithSquareCommand
from models.requests.checkout_request import CheckoutRequest
from models.requests.obtain_token_request import ObtainTokenRequest


class PaymentService:
    def __init__(self, request):
        self.request = request
        self.variables = Variables()
        self.constants = Constants()

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
        response = self.request.request(self.constants.post, self.variables.square_token_url, data=request_json,
                                        headers=headers)
        response.raise_for_status()
        response_json = json.loads(response.text)
        return response_json

    def checkout_with_square(self, command: CheckoutWithSquareCommand):
        if command.access_token == '':
            authorization_result = AuthorizeWithSquareCommand(self, {
                'grant_type': 'refresh_token',
                'refresh_token': command.refresh_token,
            }).execute()
            access_token = authorization_result['access_token']
        else:
            access_token = command.access_token
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
        response = self.request.request(self.constants.post, self.variables.square_checkout_url,
                                        data=request_json,
                                        headers=headers)
        print(response.text)
        response.raise_for_status()
        response_json = json.loads(response.text)
        return response_json