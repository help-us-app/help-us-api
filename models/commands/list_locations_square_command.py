class ListLocationsSquareCommand:
    def __init__(self, square_service, request):
        self.square_service = square_service
        self.user_id = request['user_id']

    def execute(self):
        return self.square_service.list_locations(self)
