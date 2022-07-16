class SerpResponse:
    def __init__(self, response):
        if 'title' in response:
            self.title = response['title']
        else:
            self.title = ''
        if 'description' in response:
            self.description = response['description']
        else:
            self.description = ''
        if 'thumbnail' in response:
            self.thumbnail = response['thumbnail']
        else:
            self.thumbnail = ''
        if 'rating' in response:
            self.rating = response['rating']
        else:
            self.rating = 0
        if 'reviews' in response:
            self.reviews = response['reviews']
        else:
            self.reviews = 0
        if 'seller_name' in response:
            self.seller_name = response['seller_name']
        else:
            self.seller_name = ''
        if 'quantity' in response:
            self.quantity = response['quantity']
        else:
            self.quantity = 0
        if 'product_page_url' in response:
            self.product_page_url = response['product_page_url']
        else:
            self.product_page_url = ''

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'thumbnail': self.thumbnail,
            'rating': self.rating,
            'reviews': self.reviews,
            'seller_name': self.seller_name,
            'quantity': self.quantity,
            'product_page_url': self.product_page_url,
        }
