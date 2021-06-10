"""
This app creates a REST Api using flask.
The api get items from a shop
The database for this app will be in memory, stored in a python list
API End points:
    GET    /items         : get all items
    GET    /items/<name>  : get a single item, uniquely identified by name
    POST   /items/<name>  : create an item
    PUT    /items/<name>  : update an existing item
    DELETE /items/<name>  : delete an existing item

item : {name, price}
"""
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

# Resource is like a model

app = Flask(__name__)
app.secret_key = 'password'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # create an new endpoint, /auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = next(iter(filter(lambda x: x['name'] == name, items)), None)
        return {"item": item}, 200 if item is not None else 404

    def post(self, name):
        if next(iter(filter(lambda x: x['name'] == name, items)), None) is not None:
            return {'message': f"An item with name {name} already exists"}, 400

        payload = Item.parser.parse_args()
        item = {'name': name, 'price': payload.get('price')}
        items.append(item)
        return item, 201  # 201 is http code for created

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        payload = Item.parser.parse_args()
        item = next(iter(filter(lambda x: x['name'] == name, items)), None)
        if item is None:
            item = {'name': name, 'price': payload['price']}
            items.append(item)
        else:
            item.update(payload)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
