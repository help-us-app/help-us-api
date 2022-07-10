class User:
    def __init__(self, info):
        self.id = info['id']
        self.email = info['email']
        self.password = info['password']
        if 'authorization_code' in info:
            self.authorization_code = info['authorization_code']
        if 'location_id' in info:
            self.location_id = info['location_id']
        if 'access_token' in info:
            self.access_token = info['access_token']
        if 'refresh_token' in info:
            self.refresh_token = info['refresh_token']
        if 'expires_in' in info:
            self.expires_in = info['expires_in']
        if 'merchant_id' in info:
            self.merchant_id = info['merchant_id']
