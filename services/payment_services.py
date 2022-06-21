import json
from typing import Optional

import requests as requests

from constants.constants import application_json, content_type, post, token_scopes
from constants.variables import client_id, client_secret, square_token_url
from models.requests.obtain_token_request import ObtainTokenRequest


def authorize_with_square(authorization_code, grant_type) -> Optional[str]:
    try:
        request = ObtainTokenRequest({
            'short_lived': True,
            'grant_type': grant_type,
            'client_id': client_id,
            'client_secret': client_secret,
            'scopes': token_scopes,
            'refresh_token': authorization_code,
            'code': authorization_code
        })

        request_json = json.dumps(request.to_dict())

        headers = {content_type: application_json}

        response = requests.request(post, square_token_url, data=request_json,
                                    headers=headers)

        response.raise_for_status()

        response_json = json.loads(response.text)

        return response_json

    except (Exception, requests.exceptions.RequestException) as e:
        print(f"Exception in authorize_with_square {e}")
        return None


def checkout_with_square(search_results_request) -> str:
    return "TransactionResult"
