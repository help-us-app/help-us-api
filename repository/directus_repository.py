from constants.constants import Constants
from constants.variables import Variables
from models.merchant_info import MerchantInfo


class DirectusRepository:
    def __init__(self, request):
        self.constants = Constants()
        self.variables = Variables()
        self.request = request

    def set_merchant_information_for_user(self, user_id, merchant_info: MerchantInfo):
        url = self.variables.directus_url + '/items/user/' + str(user_id)
        headers = {'Authorization': 'Bearer ' + self.variables.directus_token, self.constants.content_type : self.constants.application_json}
        data = {'merchant_id': merchant_info.merchant_id, 'access_token': merchant_info.access_token,
                'refresh_token': merchant_info.refresh_token, 'expires_in': merchant_info.expires_in}
        response = self.request.patch(url, headers=headers, data=data)
        response.raise_for_status()
        return True
