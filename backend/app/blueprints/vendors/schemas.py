from marshmallow import pre_load, validates
from app.extensions import ma
from .model import Vendor

from app.functions import (
    strip_input,
    validate_name,
    validate_address,
    validate_email_format,
    validate_phone_format,
)


class VendorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor
        load_instance = True

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("company_name")
    def check_company_name(self, value, **kwargs):
        return validate_name(value, field_name="Company name")

    @validates("address")
    def check_address(self, value, **kwargs):
        return validate_address(value)

    @validates("company_email")
    def check_company_email(self, value, **kwargs):
        return validate_email_format(value)

    @validates("company_phone")
    def check_company_phone(self, value, **kwargs):
        return validate_phone_format(value)


vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)
