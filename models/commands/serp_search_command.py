class SerpSearchCommand:
    def __init__(self, serp_service, query):
        self.serp_service = serp_service
        self.query = query

    def execute(self):
        return self.serp_service.search(self.query)

