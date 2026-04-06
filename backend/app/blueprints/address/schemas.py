from app.extensions import ma
from marshmallow import fields, pre_load, validates, ValidationError
from app.blueprints.address.model import Address
from app.functions import strip_input


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = False
        include_fk = True

    address_id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_by_user_id = fields.String(dump_only=True)
    updated_by_user_id = fields.String(dump_only=True)

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("street")
    def validate_street(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("Street is required.")

    @validates("city")
    def validate_city(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("City is required.")

    @validates("state")
    def validate_state(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("State is required.")

    @validates("zipcode")
    def validate_zipcode(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("Zip code is required.")


address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)
