from app.extensions import ma
from marshmallow import ValidationError, fields, pre_load, validates
from marshmallow import ValidationError, fields, pre_load, validates
from app.blueprints.vendor.model import Vendor
from app.functions import (
    strip_input,
    validate_city,
    validate_name,
    validate_email_format,
    validate_phone_format,
    validate_state,
    validate_street,
    validate_zipcode,
)
from app.blueprints.address.schemas import AddressSchema
from app.blueprints.address.schemas import AddressSchema


class VendorSchema(ma.SQLAlchemyAutoSchema):

    address = fields.Nested(AddressSchema, exclude=("address_id",))

    class Meta:
        model = Vendor
        load_instance = False
        include_fk = True
        exclude = ("address_id",)
        exclude = ("address_id",)

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("company_name")
    def validate_company_name(self, value, **kwargs):
        validate_name(value, field_name="Company name")

    @validates("primary_contact_name")
    def validate_primary_contact_name(self, value, **kwargs):
        validate_name(value, field_name="Primary contact name")

    @validates("company_email")
    def validate_company_email(self, value, **kwargs):
        validate_email_format(value)
    def validate_company_email(self, value, **kwargs):
        validate_email_format(value)

    @validates("company_phone")
    def validate_company_phone(self, value, **kwargs):
        validate_phone_format(value)

    @validates("service_type")
    def validate_service_type(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("Select a service type.")


vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)
