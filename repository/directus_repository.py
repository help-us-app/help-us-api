import json

from constants.constants import Constants
from constants.variables import Variables
from models.merchant_info import MerchantInfo
from models.user import User


class DirectusRepository:
    def __init__(self, request):
        self.constants = Constants()
        self.variables = Variables()
        self.request = request

    def set_merchant_information_for_user(self, user_id, merchantInfo: MerchantInfo):
        url = self.variables.directus_url + '/items/User/' + str(user_id)
        headers = {'Authorization': 'Bearer ' + self.variables.directus_token,
                   self.constants.content_type: self.constants.application_json}
        data = {'authorization_code': merchantInfo.authorization_code, 'merchant_id': merchantInfo.merchant_id,
                'access_token': merchantInfo.access_token,
                'refresh_token': merchantInfo.refresh_token, 'expires_in': merchantInfo.expires_in}
        data = json.dumps(data)
        response = self.request.patch(url, headers=headers, data=data)
        response.raise_for_status()
        return True

    def get_user_by_id(self, user_id) -> User:
        url = self.variables.directus_url + '/items/User/' + str(user_id)
        headers = {'Authorization': 'Bearer ' + self.variables.directus_token,
                   self.constants.content_type: self.constants.application_json}
        response = self.request.get(url, headers=headers)
        response.raise_for_status()
        return User(response.json()['data'])
