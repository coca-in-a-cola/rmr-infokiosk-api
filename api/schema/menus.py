from marshmallow import Schema, fields

class MenuSchema(Schema):
    type = fields.String()
    goBack = fields.Bool()
    goBackText = fields.String()

class ButtonSchema(Schema):
    text = fields.String()

