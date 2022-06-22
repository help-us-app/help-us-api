class DeleteLinkSquareCommand:
    def __init__(self, payment_service,  request):
        self.payment_service = payment_service
        self.id = request['id']
        self.access_token = request['access_token'] if 'access_token' in request else ''

    def execute(self):
        return self.payment_service.delete_link_square(self)

