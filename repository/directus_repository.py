import json

from constants.constants import Constants
from constants.variables import Variables
from models.oauth_response import OAuthResponse


class DirectusRepository:
    def __init__(self, request):
        self.constants = Constants()
        self.variables = Variables()
        self.request = request

    def set_merchant_information_for_user(self, user_id, oauth_response: OAuthResponse):
        url = self.variables.directus_url + '/items/User/' + str(user_id)
        headers = {'Authorization': 'Bearer ' + self.variables.directus_token,
                   self.constants.content_type: self.constants.application_json}
        data = {'authorization_code': oauth_response.authorization_code, 'merchant_id': oauth_response.merchant_id}
        data = json.dumps(data)
        response = self.request.patch(url, headers=headers, data=data)
        response.raise_for_status()
        return True
