import unittest
from models.responses.search_result_response import SearchResultResponse


class SearchResultResponseTests(unittest.TestCase):
    result = SearchResultResponse({
        'title': 'title',
        'link': 'link',
        'condition': 'condition',
        'price': {
            'raw': '$13.00',
            'extracted': 13,
        },
        'shipping': 'Free shipping',
        'extensions': ['or Best Offer'],
        'thumbnail': 'https://i.ebayimg.com/thumbs/images/g/0vIAAOSwOWlhitaV/s-l225.jpg',
    })

    def test_title(self) -> None:
        print('test_title')
        self.assertEqual(self.result.title, 'title')

    def test_link(self) -> None:
        print('test_link')
        self.assertEqual(self.result.link, 'link')

    def test_condition(self) -> None:
        print('test_condition')
        self.assertEqual(self.result.condition, 'condition')

    def test_price(self) -> None:
        print('test_price')
        self.assertEqual(self.result.price, {
            'raw': '$13.00',
            'extracted': 13,
        })

    def test_shipping(self) -> None:
        print('test_shipping')
        self.assertEqual(self.result.shipping, 'Free shipping')

    def test_extensions(self) -> None:
        print('test_extensions')
        self.assertEqual(self.result.extensions, ['or Best Offer'])

    def test_thumbnail(self) -> None:
        print('test_thumbnail')
        self.assertEqual(self.result.thumbnail, 'https://i.ebayimg.com/thumbs/images/g/0vIAAOSwOWlhitaV/s-l225.jpg')

    def test_to_dict(self) -> None:
        print('test_to_dict')
        self.assertEqual(self.result.to_dict(), {
            'title': 'title',
            'link': 'link',
            'condition': 'condition',
            'price': {
                'raw': '$13.00',
                'extracted': 13,
            },
            'shipping': 'Free shipping',
            'extensions': ['or Best Offer'],
            'thumbnail': 'https://i.ebayimg.com/thumbs/images/g/0vIAAOSwOWlhitaV/s-l225.jpg',
        })
