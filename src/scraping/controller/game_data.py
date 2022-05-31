import json
import os
from os.path import dirname, abspath
from typing import Dict, Any

from flask import jsonify
from jsonschema import validate


class GameData(object):
    __game_order: dict[str, Any]

    def __init__(self):
        self.__game_database = []

    def add_game_database(self, idx, page_index, game_name, game_price, game_link, game_pht):
        self.__game_order = {
            "id": idx,
            "page_indx": page_index,
            "name": game_name,
            "price": game_price,
            "game_link": game_link,
            "game_pht": game_pht
        }
        self.__game_database.append(self.__game_order)

    def home(self):
        return jsonify(self.__game_database), 200

    def delete_game(self, id):
        del self.__game_database[id - 1]
        return jsonify({'message': 'game is no longer alive'}), 200

    def save_game(self, data):
        data['id'] = self.__game_database[-1]['id'] + 1
        self.schema(data)
        if data is not None:
            self.__game_database.append(data)
            return jsonify(data), 201
        else:
            return jsonify({'error': 'not null'}), 404

    def games_per_page(self, index_page):
        games = [d for d in self.__game_database if d['page_indx'] == index_page]
        return jsonify(games), 200

    def games_per_id(self, id):
        for d in self.__game_database:
            if d['id'] == id:
                return jsonify(d), 200
        return jsonify({'error': 'game not found'}), 404

    def change_price(self, id, data):
        for d in self.__game_database:
            if d['id'] == id:
                d['price'] = data.get('price')
                return jsonify(d), 200
        return jsonify({'error': 'game not found'}), 404

    @staticmethod
    def schema(body):
        print("Os.Path {}".format(str(os.path.dirname(os.path.realpath(__file__)))))
        with open(str(os.path.dirname(os.path.realpath(__file__))) + '/schema/game_data_schema.json', 'r') as fp:
            schema = json.load(fp)
        validate(body, schema)
