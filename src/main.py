"""
This method is called when generated the packet by setup.py, or when you need to run in your IDE
"""

from flask import Flask, request

from src.scraping.orchestrator.initializer import Initializer


def create_app():

    route_initializer = Initializer()
    app = Flask(__name__)

    @app.route('/')
    def index():
        return route_initializer.endpoint

    @app.route(route_initializer.endpoint['home'], methods=['GET'])
    def route_home():
        return route_initializer.home()

    @app.route(route_initializer.endpoint['search_for_id'], methods=['GET'])
    def route_games_per_id(idx):
        return route_initializer.games_per_id(idx)

    @app.route(
        route_initializer.endpoint['search_for_index_page'], methods=['GET']
    )
    def rout_games_per_page(page):
        return route_initializer.games_per_page(page)

    @app.route(route_initializer.endpoint['home'], methods=['POST'])
    def route_save_game():
        return route_initializer.save_game(request.get_json())

    @app.route(route_initializer.endpoint['search_for_id'], methods=['PUT'])
    def route_change_price(idx):
        return route_initializer.change_price(idx, request.get_json())

    @app.route(route_initializer.endpoint['search_for_id'], methods=['DELETE'])
    def route_delete_game(idx):
        return route_initializer.delete_game(idx)

    return app


def main():
    create_app().run()


if __name__ == '__main__':
    main()
