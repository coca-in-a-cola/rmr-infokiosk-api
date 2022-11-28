from marshmallow import Schema, fields


class PColumnSchema(Schema):
    uuid = fields.String()
    title = fields.String(allow_none=True)
    size = fields.Integer()
    sortingType = fields.String(allow_none=True)


class PTableSchema(Schema):
    uuid = fields.String()
    title = fields.String(allow_none=True)
    aside = fields.String(allow_none=True)
    sort = fields.Integer()

    columns = fields.List(fields.Nested(PColumnSchema))
