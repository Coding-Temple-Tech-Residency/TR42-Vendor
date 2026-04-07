from app.extensions import ma
from marshmallow import fields, pre_load, validates
from app.blueprints.vendor.model import Vendor
from app.functions import (
    strip_input,
    validate_name,
    validate_email_format,
    validate_phone_format,
)


class VendorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor
        load_instance = False
        include_fk = True

    users = fields.Nested(
        "VendorUserSchema", many=True, dump_only=True, attribute="vendor_links"
    )
    address = fields.Nested("AddressSchema", dump_only=True)

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("company_name")
    def check_first_name(self, value, **kwargs):
        return validate_name(value, field_name="Company name")

    @validates("company_email")
    def check_email(self, value, **kwargs):
        return validate_email_format(value)

    @validates("company_phone")
    def check_company_phone(self, value, **kwargs):
        return validate_phone_format(value)


vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)
