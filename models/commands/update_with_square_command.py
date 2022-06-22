class UpdateWithSquareCommand:
    def __init__(self, payment_service, request):
        self.payment_service = payment_service
        self.id = request['id']
        if 'line_items' in request:
            self.line_items = request['line_items']
        if 'payment_note' in request:
            self.payment_note = request['payment_note']

        self.refresh_token = request['refresh_token'] if 'refresh_token' in request else ''
        self.access_token = request['access_token'] if 'access_token' in request else ''

    def execute(self):
        return self.payment_service.update(self)
