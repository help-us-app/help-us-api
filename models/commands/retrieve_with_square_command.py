class RetrieveWithSquareCommand:
    def __init__(self, square_service,  request):
        self.square_service = square_service
        self.id = request['id']
        self.access_token = request['access_token']
        self.refresh_token = request['refresh_token']
        self.expires_in = request['expires_in']

    def execute(self):
        return self.square_service.get_payment_link(self)

