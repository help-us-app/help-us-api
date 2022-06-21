import unittest

from models.requests.search_result_request import SearchResultRequest
from models.responses.search_result_response import SearchResultResponse


class SearchResultRequestTests(unittest.TestCase):

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

    response = SearchResultRequest({
        'authorizationCode': '12345',
        'searchResults': [
            result.to_dict(),
        ],
    })

    def test_authorization_code(self) -> None:
        print('test_authorization_code')
        self.assertEqual(self.response.authorization_code, '12345')

    def test_search_results(self) -> None:
        print('test_search_results')
        self.assertEqual(self.response.search_results, [
            self.result.to_dict(),
        ])

