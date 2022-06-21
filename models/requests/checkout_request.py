class CheckoutRequest:
    def __init__(self, request):
        self.order = Order(request['order'])
        self.source = request['source']

    def to_dict(self):
        return {
            'order': self.order.to_dict()
        }


class Order:
    def __init__(self, request):
        self.customer_id = request['customer_id']
        self.location_id = request['location_id']
        self.line_items = [LineItem(item) for item in request['line_items']]
        self.payment_note = request['payment_note']
        self.pre_populated_data = PrePopulatedData(request['pre_populated_data'])

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'location_id': self.location_id,
            'line_items': [item.to_dict() for item in self.line_items],
            'payment_note': self.payment_note,
            'pre_populated_data': self.pre_populated_data.to_dict()
        }


class LineItem:
    def __init__(self, request):
        self.item_type = request['item_type']
        self.name = request['name']
        self.quantity = request['quantity']
        self.base_price_money = request['base_price_money']

    def to_dict(self):
        return {
            'item_type': self.item_type,
            'name': self.name,
            'quantity': self.quantity,
            'base_price_money': self.base_price_money
        }


class PrePopulatedData:
    def __init__(self, request):
        self.buyer_email = request['buyer_email']
        self.buyer_phone_number = request['buyer_phone_number']

    def to_dict(self):
        return {
            'buyer_email': self.buyer_email,
            'buyer_phone_number': self.buyer_phone_number
        }
