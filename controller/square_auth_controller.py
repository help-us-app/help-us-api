from models.commands.authorize_with_square_command import AuthorizeWithSquareCommand
from models.commands.get_square_auth_link_command import GetSquareAuthLinkCommand
from models.commands.set_merchant_info_webhook_command import SetMerchantInfoWebHookCommand
from models.responses.obtain_token_response import ObtainTokenResponse


class SquareAuthController:
    def __init__(self, square_service):
        self.square_service = square_service

    def get_auth_link(self, user_id):
        return GetSquareAuthLinkCommand(self.square_service, user_id).execute()

    def update_merchant_information(self, request):
        response: ObtainTokenResponse = AuthorizeWithSquareCommand(self.square_service, {
            'grant_type': request['grant_type'],
            'code': request['code'],
        }).execute()

        return SetMerchantInfoWebHookCommand(self.square_service, request['user_id'],
                                             request['code'], response.merchant_id, response.access_token,
                                             response.refresh_token, response.expires_at).execute()
