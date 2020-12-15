import json
from os.path import dirname, abspath, join
from jsonschema import validate

class DataJson(object):
    def __init__(self):
        self.data_order = []
        self.id = 0

    def ad_data_order(self, page_indx, data_order, game_link, game_pht):
        self.js = {
            "id": self.id,
            "page_indx": int(page_indx),
            "name": data_order['name'],
            "price": data_order['price'],
            "game_link": game_link,
            "game_pht": game_pht
        }
        self.data_order.append(self.js)
        self.id += 1

    def schema(self,b):
        path = ""
        root = [r + "/" for r in dirname(abspath(__file__)).split("\\")]
        for r in root:
            if "source" in r:
                path += r
                break
            else:
                path += r
        with open(path + 'schema/data_order.json', 'r') as fp:
            schema = json.load(fp)
        validate(b , schema)