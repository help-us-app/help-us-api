class SetMerchantInfoWebHookCommand:
    def __init__(self, square_service, user_id, authorization_code, merchant_id, access_token, refresh_token, expires_in):
        self.square_service = square_service
        self.user_id = user_id
        self.authorization_code = authorization_code
        self.merchant_id = merchant_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in

    def execute(self):
        return self.square_service.set_merchant_information_for_user(self)
