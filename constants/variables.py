import os

from dotenv import load_dotenv


class Variables:
    def __init__(self):
        load_dotenv()
        self.directus_token = os.getenv('DIRECTUS_TOKEN')
        self.directus_url = os.getenv('DIRECTUS_URL')
        self.square_url = os.getenv('SQUARE_URL')
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.serp_url = os.getenv('SERP_URL')
        self.serp_key = os.getenv('SERP_KEY')
