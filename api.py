from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from db import get_outlet_by_source_dict, get_outlet_contains_brand_dict, get_menu_above_price_dict, insert_outlet

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return "This is the dashmote data API"


class GetOutletBySource(Resource):
    def get(self, source):
        return jsonify({'outlets': get_outlet_by_source_dict(source)})


class GetOutletContainsBrand(Resource):
    def get(self, brand):
        return jsonify({'outlets': get_outlet_contains_brand_dict(brand)})


class GetMenuAbovePrice(Resource):
    def get(self, price):
        return jsonify({'menus': get_menu_above_price_dict(float(price))})


class PostOutlet(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_outlet')
            parser.add_argument('name')
            parser.add_argument('source')
            parser.add_argument('address')
            parser.add_argument('country')
            parser.add_argument('phone')
            parser.add_argument('reviews_nr')
            outlet = parser.parse_args()
            data = {
                'id_outlet': outlet['id_outlet'],
                'name': outlet['name'],
                'source': outlet['source'],
                'address': outlet['address'],
                'country': outlet['country'],
                'phone': outlet['phone'],
                'reviews_nr': int(outlet['reviews_nr'])
            }
            insert_outlet(data)
        except Exception:
            return {'bad request': '400'}, 400
        return {'created': '201'}, 201


api.add_resource(HelloWorld, '/')
api.add_resource(GetOutletBySource, '/outlets/source/<string:source>')
api.add_resource(GetOutletContainsBrand, '/outlets/brand/contains/<string:brand>')
api.add_resource(GetMenuAbovePrice, '/menus/price/above/<string:price>')
api.add_resource(PostOutlet, '/outlets')

if __name__ == '__main__':
    app.run(debug=True)