from marshmallow import Schema, fields

class ButtonSchema(Schema):
    uuid = fields.String()
    icon = fields.String()
    link = fields.String()
    detail = fields.String()
    text = fields.String()
    onClick = fields.String()


class MenuSchema(Schema):
    uuid = fields.String()
    location = fields.String()
    type = fields.String()
    goBack = fields.Bool()
    goBackText = fields.String()
    buttons = fields.List(fields.Nested(ButtonSchema))