from marshmallow import Schema, fields

class AddressSchema(Schema):
    address_id = fields.Str(required=True)
    street = fields.Str()
    city = fields.Str()
    state = fields.Str()
    zip = fields.Str()
    country = fields.Str()
