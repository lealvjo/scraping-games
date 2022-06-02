from src.scraping.services.scraping import Scraping


class Initializer(Scraping):
    def __init__(self):
        Scraping.__init__(self)
        self.endpoint = {
            'home': '/game',
            'search_for_id': '/game/<int:idx>',
            'search_for_index_page': '/game/page/<int:page>',
        }
