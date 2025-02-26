from marshmallow import Schema, fields, validate


class PostSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=10))
    description = fields.Str(required=True)
