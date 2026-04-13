from app.extensions import ma
from marshmallow import fields, pre_load, validates, ValidationError
from app.blueprints.address.model import Address
from app.functions import (
    strip_input,
    validate_city,
    validate_state,
    validate_street,
    validate_zipcode,
)


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = False
        include_fk = True

        dump_only = (
            "address_id",
            "created_at",
            "updated_at",
            "created_by_user_id",
            "updated_by_user_id",
        )

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("street")
    def validate_address_field(self, value, **kwargs):
        validate_street(value)

    @validates("city")
    def validate_city_field(self, value, **kwargs):
        validate_city(value)

    @validates("state")
    def validate_state_field(self, value, **kwargs):
        validate_state(value)

    @validates("zipcode")
    def validate_zipcode_field(self, value, **kwargs):
        validate_zipcode(value)


address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)
