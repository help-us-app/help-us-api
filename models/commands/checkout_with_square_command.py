class CheckoutWithSquareCommand:
    def __init__(self, payment_service, request):
        self.payment_service = payment_service
        self.refresh_token = request['refresh_token'] if 'refresh_token' in request else ''
        self.location_id = request['location_id']
        self.customer_id = request['customer_id']
        self.line_items = request['line_items']
        self.buyer_email = request['buyer_email']
        self.buyer_phone_number = request['buyer_phone_number']
        self.payment_note = request['payment_note']
        self.access_token = request['access_token'] if 'access_token' in request else ''

    def execute(self):
        return self.payment_service.checkout_with_square(self)
