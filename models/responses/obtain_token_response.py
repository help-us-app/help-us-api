class ObtainTokenResponse:

    def __init__(self, response) -> None:
        self.access_token = response['access_token']
        self.merchant_id = response['merchant_id']
        self.refresh_token = response['refresh_token']
        self.short_lived = response['short_lived']
        self.expires_at = response['expires_at']

    def to_dict(self) -> dict:
        return {
            'access_token': self.access_token,
            'merchant_id': self.merchant_id,
            'refresh_token': self.refresh_token,
            'short_lived': self.short_lived,
            'expires_at': self.expires_at
        }


