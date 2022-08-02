class PaymentSquareWebhookCommand:
    def __init__(self, square_service, request):
        self.buyer_email = request['buyer_email']
        self.square_service = square_service
        self.item_ids = request['item_ids']

    def execute(self):
        return self.square_service.update_items_status_to_complete(self.item_ids)
