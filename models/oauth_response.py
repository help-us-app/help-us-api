class OAuthResponse:
    def __init__(self, info):
        self.authorization_code = info['authorization_code']
        self.merchant_id = info['merchant_id']

