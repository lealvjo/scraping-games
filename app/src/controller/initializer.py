from app.src.services.scraping import Scraping


class Initializer(Scraping):
    def __init__(self):
        Scraping.__init__(self)
        self.get_promotions()
        self.endpoint = {
            'home': '/python/game',
            'search_for_id': '/python/game/<int:id>',
            'search_for_index_page': '/python/game/page/<int:page>'
        }
