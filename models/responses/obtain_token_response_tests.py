import unittest

from models.responses.obtain_token_response import ObtainTokenResponse


class ObtainTokenRequestTests(unittest.TestCase):

    response = ObtainTokenResponse({
        'short_lived': True,
        'merchant_id': '12345',
        'access_token': 'abcdefg',
        'refresh_token': 'hijklmnop'
    })

    def test_short_lived(self) -> None:
        print('test_short_lived')
        self.assertEqual(self.response.short_lived, True)

    def test_merchant_id(self) -> None:
        print('test_merchant_id')
        self.assertEqual(self.response.merchant_id, '12345')

    def test_access_token(self) -> None:
        print('test_access_token')
        self.assertEqual(self.response.access_token, 'abcdefg')

    def test_refresh_token(self) -> None:
        print('test_refresh_token')
        self.assertEqual(self.response.refresh_token, 'hijklmnop')

    def test_to_dict(self) -> None:
        print('test_to_dict')
        self.assertEqual(self.response.to_dict(), {
            'short_lived': True,
            'merchant_id': '12345',
            'access_token': 'abcdefg',
            'refresh_token': 'hijklmnop'
        })



