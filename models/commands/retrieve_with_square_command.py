class RetrieveWithSquareCommand:
    def __init__(self, payment_service,  request):
        self.payment_service = payment_service
        self.id = request['id']
        self.access_token = request['access_token'] if 'access_token' in request else ''

    def execute(self):
        return self.payment_service.get_payment_link(self)

