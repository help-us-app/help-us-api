import os

from dotenv import load_dotenv


class Variables:
    def __init__(self):
        load_dotenv()
        self.square_checkout_url = os.getenv('SQUARE_CHECKOUT_URL')
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.square_token_url = os.getenv('SQUARE_TOKEN_URL')
        self.square_webhook_url_transaction_success = os.getenv('SQUARE_WEBHOOK_URL_TRANSACTION_SUCCESS')
