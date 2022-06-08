from marshmallow import Schema, fields

class UserSchema(Schema):
    fullname = fields.String()
    personnel_number = fields.String()
    subdivision = fields.String()
    position = fields.String()
    phone_number = fields.String()