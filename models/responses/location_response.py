class LocationResponse:
    def __init__(self, result):
        self.location = Location(result['location'])

    def to_dict(self):
        return {
            'location': self.location.to_dict()
        }


class Location:
    def __init__(self, result):
        self.id = result['id']
        self.name = result['name']
        self.address = Address(result['address'])
        self.status = result['status']
        self.merchant_id = result['merchant_id']
        self.country = result['country']
        self.language_code = result['language_code']
        self.currency = result['currency']
        self.business_name = result['business_name']
        self.business_email = result['business_email']
        self.logo_url = result['logo_url']
        self.pos_background_url = result['pos_background_url']

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address.to_dict(),
            'status': self.status,
            'merchant_id': self.merchant_id,
            'country': self.country,
            'language_code': self.language_code,
            'currency': self.currency,
            'business_name': self.business_name,
            'business_email': self.business_email,
            'logo_url': self.logo_url,
            'pos_background_url': self.pos_background_url
        }


class Address:
    def __init__(self, result):
        self.address_line_1 = result['address_line_1']
        self.locality = result['locality']
        self.administrative_district_level_1 = result['administrative_district_level_1']
        self.postal_code = result['postal_code']
        self.country = result['country']

    def to_dict(self):
        return {
            'address_line_1': self.address_line_1,
            'locality': self.locality,
            'administrative_district_level_1': self.administrative_district_level_1,
            'postal_code': self.postal_code,
            'country': self.country
        }
