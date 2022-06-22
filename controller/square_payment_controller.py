from models.commands.authorize_with_square_command import AuthorizeWithSquareCommand
from models.commands.checkout_with_square_command import CheckoutWithSquareCommand
from models.commands.delete_link_square_command import DeleteLinkSquareCommand
from models.commands.retrieve_with_square_command import RetrieveWithSquareCommand
from models.commands.update_with_square_command import UpdateWithSquareCommand


class SquarePaymentController:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def authorize(self, request):
        return AuthorizeWithSquareCommand(self.payment_service, request).execute()

    def create(self, request):
        return CheckoutWithSquareCommand(self.payment_service, request).execute()

    def delete(self, request):
        return DeleteLinkSquareCommand(self.payment_service, request).execute()

    def read(self, request):
        return RetrieveWithSquareCommand(self.payment_service, request).execute()

    def update(self, request):
        return UpdateWithSquareCommand(self.payment_service, request).execute()


