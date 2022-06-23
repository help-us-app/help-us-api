class MerchantInfo:
    def __init__(self, info):
        self.merchant_id = info['merchant_id']
        self.access_token = info['access_token']
        self.refresh_token = info['refresh_token']
        self.expires_in = info['expires_in']
