import requests
from bs4 import BeautifulSoup
from app.src.controller.data_json import DataJson


class Scraping(DataJson):
    def __init__(self):
        DataJson.__init__(self)
        self.nuuvem_url = "https://www.nuuvem.com/"
        print("Collecting promotions {}".format(self.nuuvem_url))

    def get_promotions(self):
        self.web = requests.get(self.nuuvem_url + "fpromo/nintendo?utm_source=Nintendo&utm_medium=landing_page")
        try:
            self.__get_atrib_game()
        except:
            print("shocked climb :( ")
            self.ad_data_order(0, 1, 'Game Mock', 'R$ 00,00', 'https://mock', 'https://mock.jpg')

    def __get_atrib_game(self):
        self.web_page = BeautifulSoup(self.web.text, "html.parser")
        products_list = self.web_page.find('div', {'class',
                                                   'products-dock--main nvm-mod mod-group-sell mod-group-sell-offer'}).find_all(
            'div', {'class', 'product-card--grid'})
        for p in products_list:
            util = p.find('div', {'class',
                                  'product__available product__purchasable product-card product-card__cover product-btn-add-to-cart--container'})

            self.ad_data_order(products_list.index(p),
                               1,
                               util.get('data-track-product-name'),
                               util.get('data-track-product-price'),
                               util.get('data-track-product-url'),
                               util.get('data-track-product-image-url'),
                               )
