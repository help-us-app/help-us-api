class CheckoutResponse:
    def __init__(self, result):
        self.payment_link = PaymentLink(result['payment_link'])

    def to_dict(self):
        return {
            'payment_link': self.payment_link.to_dict()
        }


class PaymentLink:
    def __init__(self, result):
        self.created_at = result['created_at']
        self.id = result['id']
        self.order_id = result['order_id']
        self.url = result['url']
        self.version = result['version']

    def to_dict(self):
        return {
            'created_at': self.created_at,
            'id': self.id,
            'order_id': self.order_id,
            'url': self.url,
            'version': self.version
        }
