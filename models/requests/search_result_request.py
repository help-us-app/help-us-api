class SearchResultRequest:

    def __init__(self, request):
        self.authorization_code = request['authorizationCode']
        self.search_results = request['searchResults']
