from models.commands.serp_search_command import SerpSearchCommand


class SerpController:
    def __init__(self, serp_service):
        self.serp_service = serp_service

    def search(self, query):
        return SerpSearchCommand(self.serp_service, query).execute()
