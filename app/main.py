from flask import Flask
from flask import jsonify

app = Flask(__name__)


stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return 'Hello World><'


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8000,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
