from flask import Flask, jsonify
from flask_restful import Resource, Api
from db import get_outlet_by_source_dict, get_outlet_contains_brand_dict, get_menu_above_price_dict

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
        return jsonify({'menus': get_menu_above_price_dict(price)})


api.add_resource(HelloWorld, '/')
api.add_resource(GetOutletBySource, '/outlets/source/<string:source>')
api.add_resource(GetOutletContainsBrand, '/outlets/brand/<string:brand>')
api.add_resource(GetMenuAbovePrice, '/menus/price/<float:price>')

if __name__ == '__main__':
    app.run(debug=True)