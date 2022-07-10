
class GetSquareAuthLinkCommand:
    def __init__(self, square_service,user_id):
        self.square_service = square_service
        self.user_id = user_id

    def execute(self):
        return self.square_service.get_square_auth_link(self.user_id)
