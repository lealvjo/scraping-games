import requests
from bs4 import BeautifulSoup
from loguru import logger

from src.scraping.controller.game_data import GameData


class Scraping(GameData):
    def __init__(self):
        GameData.__init__(self)
        self.web = requests.get(
            'https://www.nuuvem.com/promo/nintendo?utm_source=Nintendo&utm_medium=landing_page'
        )
        logger.info(
            'Collecting promotions {}'.format('https://www.nuuvem.com/promo')
        )

    def get_games_collection(self):
        try:
            self.__get_attribute_game()
            logger.info(f'Success colection :) - {self.web.status_code}')
        except:
            logger.info(f'shocked climb :( {self.web.status_code}')
            self.add_game_database(
                0,
                1,
                'The Legend of Zelda - Breath of the Wild',
                'R$ 299,00',
                'https://www.nintendo.com/pt_BR/games/detail/the-legend-of-zelda-breath-of-the-wild-switch/',
                'https://assets.nintendo.com/image/upload/c_pad,f_auto,h_613,q_auto,'
                'w_1089/ncom/pt_BR/games/switch/t/the-legend-of-zelda-breath-of-the-wild-switch/hero?v=2022042121',
            )

    def __get_attribute_game(self):
        self.web_page = BeautifulSoup(self.web.text, 'html.parser')
        products_list = self.web_page.find(
            'div',
            {
                'class',
                'products-dock--main nvm-mod mod-group-sell mod-group-sell-offer',
            },
        ).find_all('div', {'class', 'product-card--grid'})
        for p in products_list:
            util = p.find(
                'div',
                {
                    'class',
                    'product__available product__purchasable product-card product-card__cover '
                    'product-btn-add-to-cart--container',
                },
            )

            self.add_game_database(
                products_list.index(p),
                1,
                util.get('data-track-product-name'),
                util.get('data-track-product-price'),
                util.get('data-track-product-url'),
                util.get('data-track-product-image-url'),
            )
