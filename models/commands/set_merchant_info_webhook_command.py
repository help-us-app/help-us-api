class SetMerchantInfoWebHookCommand:
    def __init__(self, square_service, user_id, authorization_code, merchant_id):
        self.square_service = square_service
        self.user_id = user_id
        self.authorization_code = authorization_code
        self.merchant_id = merchant_id

    def execute(self):
        return self.square_service.set_merchant_information_for_user(self)
