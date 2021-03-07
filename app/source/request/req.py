from app.source.services.scraping import Scraping

class Req(Scraping):
    def __init__(self):
        Scraping.__init__(self)
        self.get_promotions()
        self.endpoint = {
            'home': '/game',
            'search_for_id': '/game/<int:id>',
            'search_for_index_ps_page': '/game/page/<int:page>'
        }