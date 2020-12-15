'''
This method is called when generated the packet by setup.py, or when you need to run in your IDE
'''

from flask import Flask, jsonify, request
from app.source.request.req import Req

r = Req()
app = Flask(__name__)


@app.route(r.endpoint['home'], methods=['GET'])
def home():
    return jsonify(r.data_order), 200


@app.route(r.endpoint['search_for_id'], methods=['GET'])
def games_per_id(id):
    for d in r.data_order:
        if d['id'] == id:
            return jsonify(d), 200
    return jsonify({'error': 'game not found'}), 404


@app.route(r.endpoint['search_for_index_ps_page'], methods=['GET'])
def games_per_page(page):
    games = [d for d in r.data_order if d['page_indx'] == page]
    return jsonify(games), 200


@app.route(r.endpoint['home'], methods=['POST'])
def save_game():
    data = request.get_json()
    data['id'] = r.data_order[-1]['id'] + 1
    r.schema(data)
    if data is not None:
        r.data_order.append(data)
        return jsonify(data), 201
    else:
        return jsonify({'error': 'not null'}), 404


@app.route(r.endpoint['search_for_id'], methods=['PUT'])
def change_price(id):
    for d in r.data_order:
        if d['id'] == id:
            d['price'] = request.get_json().get('price')
            return jsonify(d), 200
    return jsonify({'error': 'game not found'}), 404


@app.route(r.endpoint['search_for_id'], methods=['DELETE'])
def remove_game(id):
    index = id - 1
    del r.data_order[index]
    return jsonify({'message': 'game is no longer alive'}), 200


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()