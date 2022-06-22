
class GetSquareAuthLinkCommand:
    def __init__(self, square_service):
        self.square_service = square_service

    def execute(self):
        return self.square_service.get_square_auth_link()
