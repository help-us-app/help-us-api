class ObtainTokenRequest:

    def __init__(self, response) -> None:
        self.short_lived = response['short_lived']
        self.grant_type = response['grant_type']
        self.client_id = response['client_id']
        self.client_secret = response['client_secret']
        self.scopes = response['scopes']
        self.code = response['code']

    def to_dict(self) -> dict:
        return {
            'short_lived': self.short_lived,
            'grant_type': self.grant_type,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scopes': self.scopes,
            'code': self.code
        }


