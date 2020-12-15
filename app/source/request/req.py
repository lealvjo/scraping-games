from app.source.ps_store.ps_scraping import PsScraping

class Req(PsScraping):
    def __init__(self):
        PsScraping.__init__(self)
        self.get_ps_store()
        self.endpoint = {
            'home': '/game',
            'search_for_id': '/game/<int:id>',
            'search_for_index_ps_page': '/game/page/<int:page>'
        }