from models.responses.checkout_response import CheckoutResponse


class AuthorizeWithSquareCommand:
    def __init__(self, payment_service, request):
        self.payment_service = payment_service
        self.grant_type = request['grant_type']
        self.refresh_token = request['refresh_token'] if 'refresh_token' in request else ''
        self.code = request['code'] if 'code' in request else ''

    def execute(self) -> CheckoutResponse:
        return self.payment_service.authorize_with_square(self)
