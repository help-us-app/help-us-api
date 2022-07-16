from constants.constants import Constants
from constants.variables import Variables
from models.responses.serp_response import SerpResponse
from repository.directus_repository import DirectusRepository


class SerpService:
    def __init__(self, request):
        self.request = request
        self.variables = Variables()
        self.constants = Constants()
        self.directus_repository = DirectusRepository(self.request)

    def search(self, query):
        response = self.request.get(self.variables.serp_url, params={
            "query": query,
            "engine": self.constants.serp_api_engine,
            "api_key": self.variables.serp_key,
        })
        response.raise_for_status()

        for item in response.json()['organic_results']:
            yield SerpResponse(item)
