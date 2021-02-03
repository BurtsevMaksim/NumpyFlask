from flask import Flask
from flask_restful import Api, Resource
from constants import DistanceData, API_KEY_NAME, API_KEY_VALUE
from flask_httpauth import HTTPTokenAuth
import json

app = Flask(__name__)
api = Api(app)
auth = HTTPTokenAuth(header=API_KEY_NAME)


@auth.verify_token
def verify_token(token):
    if token == API_KEY_VALUE:
        return API_KEY_VALUE


class Endpoint(Resource):
    @auth.login_required
    def get(self):
        return json.dumps((DistanceData(1488, 1488).__dict__))


api.add_resource(Endpoint, "/")

if __name__ == "__main__":
    app.run(debug=True)
