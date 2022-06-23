from models.commands.authorize_with_square_command import AuthorizeWithSquareCommand
from models.commands.get_square_auth_link_command import GetSquareAuthLinkCommand


class SquareAuthController:
    def __init__(self, square_service):
        self.square_service = square_service

    def authorize(self, request):
        return AuthorizeWithSquareCommand(self.square_service, request).execute()

    def get_auth_link(self):
        return GetSquareAuthLinkCommand(self.square_service).execute()

