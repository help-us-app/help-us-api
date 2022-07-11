class MerchantInfo:
    def __init__(self, info):
        if 'merchant_id' in info:
            self.merchant_id = info['merchant_id']
        self.access_token = info['access_token']
        self.refresh_token = info['refresh_token']
        self.expires_in = info['expires_in']
        if 'authorization_code' in info:
            self.authorization_code = info['authorization_code']
