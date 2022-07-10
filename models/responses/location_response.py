class LocationResponse:
    def __init__(self, result):
        self.location = Location(result['location'])

    def to_dict(self):
        return {
            'location': self.location.to_dict()
        }


class Location:
    def __init__(self, result):
        if 'id' in result:
            self.id = result['id']
        else:
            self.id = ''
        if 'name' in result:
            self.name = result['name']
        else:
            self.name = ''
        if 'address' in result:
            self.address = Address(result['address'])
        else:
            self.address = Address({})
        if 'status' in result:
            self.status = result['status']
        else:
            self.status = ''
        if 'merchant_id' in result:
            self.merchant_id = result['merchant_id']
        else:
            self.merchant_id = ''
        if 'country' in result:
            self.country = result['country']
        else:
            self.country = ''
        if 'language_code' in result:
            self.language_code = result['language_code']
        else:
            self.language_code = ''
        if 'currency' in result:
            self.currency = result['currency']
        else:
            self.currency = ''
        if 'business_name' in result:
            self.business_name = result['business_name']
        else:
            self.business_name = ''
        if 'business_email' in result:
            self.business_email = result['business_email']
        else:
            self.business_email = ''
        if 'logo_url' in result:
            self.logo_url = result['logo_url']
        else:
            self.logo_url = ''
        if 'pos_background_url' in result:
            self.pos_background_url = result['pos_background_url']
        else:
            self.pos_background_url = ''
        if 'description' in result:
            self.description = result['description']
        else:
            self.description = ''

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
            'description': self.description,
            'logo_url': self.logo_url,
            'pos_background_url': self.pos_background_url
        }


class Address:
    def __init__(self, result):
        if 'address_line_1' in result:
            self.address_line_1 = result['address_line_1']
        if 'locality' in result:
            self.locality = result['locality']
        if 'administrative_district_level_1' in result:
            self.administrative_district_level_1 = result['administrative_district_level_1']
        if 'postal_code' in result:
            self.postal_code = result['postal_code']
        if 'country' in result:
            self.country = result['country']

    def to_dict(self):
        return {
            'address_line_1': self.address_line_1,
            'locality': self.locality,
            'administrative_district_level_1': self.administrative_district_level_1,
            'postal_code': self.postal_code,
            'country': self.country
        }
