from models.commands.list_locations_square_command import ListLocationsSquareCommand
from models.commands.retrieve_location_square_command import RetrieveLocationSquareCommand


class SquareLocationController:
    def __init__(self, square_service):
        self.square_service = square_service

    def get_location_information(self, request):
        return RetrieveLocationSquareCommand(self.square_service, request).execute()

    def list_locations(self, request):
        return ListLocationsSquareCommand(self.square_service, request).execute()
