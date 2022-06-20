class SearchResultResponse:
    def __init__(self, result):
        self.title = result['title']
        self.link = result['link']
        self.condition = result['condition']
        self.price = result['price']
        self.shipping = result['shipping']
        self.extensions = result['extensions']
        self.thumbnail = result['thumbnail']

    def to_dict(self):
        return {
            'title': self.title,
            'link': self.link,
            'condition': self.condition,
            'price': self.price,
            'shipping': self.shipping,
            'extensions': self.extensions,
            'thumbnail': self.thumbnail
        }
