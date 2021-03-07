import json
from os.path import dirname, abspath
from jsonschema import validate

class DataJson(object):
    def __init__(self):
        self.data_order = []
        self.id = 0

    def ad_data_order(self, id, page_indx, game_name, game_price, game_link, game_pht):
        self.js = {
            "id": id,
            "page_indx": page_indx,
            "name": game_name,
            "price": game_price,
            "game_link": game_link,
            "game_pht": game_pht
        }
        self.data_order.append(self.js)

    def schema(self, body):
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
        validate(body, schema)