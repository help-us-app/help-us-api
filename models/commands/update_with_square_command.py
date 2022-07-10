class UpdateWithSquareCommand:
    def __init__(self, square_service, request):
        self.square_service = square_service
        self.id = request['id']
        if 'line_items' in request:
            self.line_items = request['line_items']
        if 'payment_note' in request:
            self.payment_note = request['payment_note']
        self.user_id = request['user_id']

    def execute(self):
        return self.square_service.update_with_square(self)
