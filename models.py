from flask import request
from flask_restful import Resource


class Endpoint(Resource):
    def get(self):
        return request.args