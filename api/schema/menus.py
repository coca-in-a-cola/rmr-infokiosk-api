from marshmallow import Schema, fields
    
class MenuSchema(Schema):

    class ButtonSchema(Schema):
        icon = fields.String()
        link = fields.String()
        detail = fields.String()
        text = fields.String()
        onClick = fields.String()


    type = fields.String()
    goBack = fields.Bool()
    goBackText = fields.String()
    buttons = fields.List(fields.Nested(ButtonSchema))