import json
from os.path import dirname, abspath
from flask import jsonify
from jsonschema import validate


class DataJson(object):
    def __init__(self):
        self.data_order = []

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

    def delete_game(self, id):
        del self.data_order[id - 1]
        return jsonify({'message': 'game is no longer alive'}), 200

    def save_game(self, data):
        data['id'] = self.data_order[-1]['id'] + 1
        self.schema(data)
        if data is not None:
            self.data_order.append(data)
            return jsonify(data), 201
        else:
            return jsonify({'error': 'not null'}), 404

    def games_per_page(self, index_page):
        games = [d for d in self.data_order if d['page_indx'] == index_page]
        return jsonify(games), 200

    def games_per_id(self, id):
        for d in self.data_order:
            if d['id'] == id:
                return jsonify(d), 200
        return jsonify({'error': 'game not found'}), 404

    def home(self):
        return jsonify(self.data_order), 200

    def change_price(self, id, data):
        for d in self.data_order:
            if d['id'] == id:
                d['price'] = data.get('price')
                return jsonify(d), 200
        return jsonify({'error': 'game not found'}), 404

    def schema(self, body):
        path = ""
        root = [r + "/" for r in dirname(abspath(__file__)).split("\\")]
        for r in root:
            if "src" in r:
                path += r
                break
            else:
                path += r
        with open(path + 'schema/data_order.json', 'r') as fp:
            schema = json.load(fp)
        validate(body, schema)