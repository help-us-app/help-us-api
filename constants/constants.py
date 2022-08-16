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
        self.token_scopes = ['MERCHANT_PROFILE_READ', 'PAYMENTS_READ', 'ORDERS_READ', 'ORDERS_WRITE', 'PAYMENTS_WRITE']
        self.payment_link_endpoint = 'online-checkout/payment-links/'
        self.obtain_token_endpoint = 'oauth2/token'
        self.authorize_endpoint = 'oauth2/authorize'
        self.version = 'v2/'
        self.amazon_cart_url = 'https://www.amazon.com/gp/cart/view.html?ref_=nav_cart'
