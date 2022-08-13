from marshmallow import Schema, fields

class PerformerSchema(Schema):
    uuid = fields.String()
    uuid_1c = fields.String()
    fullname = fields.String()
    completionTimeInHours = fields.Integer()
    responsible = fields.Boolean()


class FormFieldSchema(Schema):
    uuid = fields.String()
    id = fields.String(allow_none=True)
    label = fields.String(allow_none=True)
    type = fields.String(allow_none=True)
    value = fields.String(allow_none=True)
    name = fields.String(allow_none=True)
    min = fields.String(allow_none=True)
    max = fields.String(allow_none=True)


class FormTaskSchema(Schema):
    uuid = fields.String()
    title = fields.String(allow_none=True)
    completionTimeInHours = fields.Integer()
    performers = fields.List(fields.Nested(PerformerSchema))
    fields = fields.List(fields.Nested(FormFieldSchema))

