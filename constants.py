from marshmallow import Schema, fields


class QuerySchema(Schema):
    start = fields.Str(required=True)
    end = fields.Str(required=True)


class DistanceData:
    def __init__(self, path, distance):
        self.path = None
        self.distance = None


SCHEMA = QuerySchema
