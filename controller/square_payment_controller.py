from models.commands.checkout_with_square_command import CheckoutWithSquareCommand
from models.commands.delete_link_square_command import DeleteLinkSquareCommand
from models.commands.retrieve_with_square_command import RetrieveWithSquareCommand
from models.commands.update_with_square_command import UpdateWithSquareCommand


class SquarePaymentController:
    def __init__(self, square_service):
        self.square_service = square_service

    def create(self, request):
        return CheckoutWithSquareCommand(self.square_service, request).execute()

    def delete(self, request):
        return DeleteLinkSquareCommand(self.square_service, request).execute()

    def read(self, request):
        return RetrieveWithSquareCommand(self.square_service, request).execute()

    def update(self, request):
        return UpdateWithSquareCommand(self.square_service, request).execute()
