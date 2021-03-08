'''
This method is called when generated the packet by setup.py, or when you need to run in your IDE
'''

from flask import Flask, request
from app.src.controller.initializer import Initializer

route_initializer = Initializer()
app = Flask(__name__)


@app.route(route_initializer.endpoint['home'], methods=['GET'])
def route_home():
    return route_initializer.home()


@app.route(route_initializer.endpoint['search_for_id'], methods=['GET'])
def route_games_per_id(id):
    return route_initializer.games_per_id(id)


@app.route(route_initializer.endpoint['search_for_index_page'], methods=['GET'])
def rout_games_per_page(page):
    return route_initializer.games_per_page(page)


@app.route(route_initializer.endpoint['home'], methods=['POST'])
def route_save_game():
    return route_initializer.save_game(request.get_json())


@app.route(route_initializer.endpoint['search_for_id'], methods=['PUT'])
def route_change_price(id):
    return route_initializer.change_price(id, request.get_json())


@app.route(route_initializer.endpoint['search_for_id'], methods=['DELETE'])
def route_delete_game(id):
    return route_initializer.delete_game(id)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
