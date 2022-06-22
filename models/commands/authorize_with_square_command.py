from models.responses.obtain_token_response import ObtainTokenResponse


class AuthorizeWithSquareCommand:
    def __init__(self, payment_service, request):
        self.payment_service = payment_service
        self.grant_type = request['grant_type']
        self.refresh_token = request['refresh_token'] if 'refresh_token' in request else ''
        self.code = request['code'] if 'code' in request else ''

    def execute(self) -> ObtainTokenResponse:
        return self.payment_service.authorize(self)
