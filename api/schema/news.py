from marshmallow import Schema, fields

class NewsEntrySchema(Schema):
    url = fields.String()
    title = fields.String()

    