from models.requests.obtain_token_request import ObtainTokenRequest
import unittest


class ObtainTokenRequestTests(unittest.TestCase):
    response = ObtainTokenRequest({
        'short_lived': True,
        'grant_type': 'authorization_code',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'scopes': ['scope1', 'scope2'],
        'code': 'code',
        'refresh_token': 'refresh_token'
    })

    def test_short_lived(self) -> None:
        print('test_short_lived')
        self.assertEqual(self.response.short_lived, True)

    def test_grant_type(self) -> None:
        print('test_grant_type')
        self.assertEqual(self.response.grant_type, 'authorization_code')

    def test_client_id(self) -> None:
        print('test_client_id')
        self.assertEqual(self.response.client_id, 'client_id')

    def test_client_secret(self) -> None:
        print('test_client_secret')
        self.assertEqual(self.response.client_secret, 'client_secret')

    def test_scopes(self) -> None:
        print('test_scopes')
        self.assertEqual(self.response.scopes, ['scope1', 'scope2'])

    def test_code(self) -> None:
        print('test_code')
        self.assertEqual(self.response.code, 'code')

    def test_refresh_token(self) -> None:
        print('test_refresh_token')
        self.assertEqual(self.response.refresh_token, 'refresh_token')

    def test_to_dict(self) -> None:
        print('test_to_dict')
        self.assertEqual(self.response.to_dict(), {
            'short_lived': True,
            'grant_type': 'authorization_code',
            'client_id': 'client_id',
            'client_secret': 'client_secret',
            'scopes': ['scope1', 'scope2'],
            'code': 'code',
            'refresh_token': 'refresh_token'
        })
