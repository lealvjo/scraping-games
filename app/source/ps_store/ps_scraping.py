import requests
import json
from bs4 import BeautifulSoup
from app.source.data_order.data_json import DataJson

class PsScraping(DataJson):
    def __init__(self):
        DataJson.__init__(self)
        self.ps_url = "https://store.playstation.com"
        print("Collecting promotions {}".format(self.ps_url))
        self.index = ["1"]
        self.index_r = []

    def get_ps_store(self):
        for self.page_indx in self.index:
            if self.page_indx not in self.index_r:
                self.web = requests.get(self.ps_url + "/pt-br/category/35027334-375e-423b-b500-0d4d85eff784/" + self.page_indx)
                self.get_pagination()
                self.get_atrib_game()
                self.index_r.append(self.page_indx)

    def get_pagination(self):
        self.web_page = BeautifulSoup(self.web.text, "html.parser")
        pagi = self.web_page.find_all("div", {"class": "ems-sdk-grid-paginator__page-button"})
        for p in pagi:
            self.index.append(p.find("button").text)

    def get_atrib_game(self):
        self.web_page = BeautifulSoup(self.web.text, "html.parser")
        game_list = self.web_page.find("div", {"class":"ems-sdk-grid__body psw-cell psw-mobile-p-12"}).find_all("li")
        for game in game_list:
            game_json = json.loads(game.find('div', {'class': 'ems-sdk-product-tile'}).find('a').get('data-telemetry-meta'))
            game_link = game.find('div', {'class': 'ems-sdk-product-tile'}).find('a').get('href')
            game_pht = game.find('div', {'class':'ems-sdk-product-tile-image__container'}).find_all("img")
            self.ad_data_order(self.page_indx, game_json, self.ps_url + game_link, game_pht[1]['src'])
