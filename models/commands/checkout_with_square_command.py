class CheckoutWithSquareCommand:
    def __init__(self, square_service, request):
        self.square_service = square_service
        self.user_id = request['user_id']
        self.location_id = request['location_id']
        self.customer_id = request['customer_id']
        self.line_items = request['line_items']
        self.buyer_email = request['buyer_email']
        self.buyer_phone_number = request['buyer_phone_number']
        self.payment_note = request['payment_note']

    def execute(self):
        return self.square_service.checkout_with_square(self)
