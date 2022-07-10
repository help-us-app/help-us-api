class Constants:
    def __init__(self):
        self.location_endpoint = "locations/"
        self.put = 'PUT'
        self.get = 'GET'
        self.delete = 'DELETE'
        self.app_name = "help us app"
        self.application_json = "application/json"
        self.content_type = "Content-Type"
        self.post = "POST"
        self.token_scopes = ['MERCHANT_PROFILE_READ', 'PAYMENTS_READ']
        self.payment_link_endpoint = 'online-checkout/payment-links/'
        self.obtain_token_endpoint = 'oauth2/token'
        self.authorize_endpoint = 'oauth2/authorize'
        self.version = 'v2/'
