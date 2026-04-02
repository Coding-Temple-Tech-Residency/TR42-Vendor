from app.extensions import ma
from marshmallow import fields
from app.blueprints.vendor.model import Vendor


class VendorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor
        load_instance = True
        include_fk = True


    users = fields.Nested("VendorUserSchema", many=True, dump_only=True)

    # MUST be a STRING — not a class reference
    address = fields.Nested("AddressSchema")


vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)


# -----------------------------
# Registration Schemas
# -----------------------------
class UserRegistrationSchema(ma.Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)


class VendorRegistrationSchema(ma.Schema):
    company_name = fields.String(required=True)
    company_email = fields.Email(required=True)
    company_phone = fields.String(required=True)
    service_type = fields.String(required=True)


class AddressRegistrationSchema(ma.Schema):
    street = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zipcode = fields.String(required=True)


class CombinedVendorRegistrationSchema(ma.Schema):
    user = fields.Nested(UserRegistrationSchema, required=True)
    vendor = fields.Nested(VendorRegistrationSchema, required=True)
    address = fields.Nested(AddressRegistrationSchema, required=True)
