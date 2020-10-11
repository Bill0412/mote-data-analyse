from flask import Flask, jsonify
from flask_restful import Resource, Api
from db import get_outlet_by_source_dict

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return "This is the dashmote data API"


class GetOutletBySource(Resource):
    def get(self, source):
        ret = get_outlet_by_source_dict(source)
        print(ret)
        return jsonify({'outlets': ret})


api.add_resource(HelloWorld, '/')
api.add_resource(GetOutletBySource, '/outlets/source/<string:source>')

if __name__ == '__main__':
    app.run(debug=True)