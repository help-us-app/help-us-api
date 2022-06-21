import os

from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
square_token_url = os.getenv('SQUARE_TOKEN_URL')