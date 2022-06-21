from models.commands.authorize_with_square_command import AuthorizeWithSquareCommand
from models.commands.checkout_with_square_command import CheckoutWithSquareCommand
from models.commands.delete_link_square_command import DeleteLinkSquareCommand


class PaymentController:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def authorize_with_square(self, request):
        return AuthorizeWithSquareCommand(self.payment_service, request).execute()

    def checkout_with_square(self, request):
        return CheckoutWithSquareCommand(self.payment_service, request).execute()

    def delete_link_square(self, request):
        return DeleteLinkSquareCommand(self.payment_service, request).execute()


