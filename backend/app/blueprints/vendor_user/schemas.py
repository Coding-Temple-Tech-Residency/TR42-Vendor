from app.extensions import ma
from marshmallow import fields
from app.blueprints.vendor_user.model import VendorUser


class VendorUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VendorUser
        load_instance = False
        include_fk = True

    vendor = fields.Nested(
        "VendorSchema",
        dump_only=True,
        exclude=("vendor_links", "address"),
    )

    user = fields.Nested(
        "UserSchema",
        dump_only=True,
    )


vendor_user_schema = VendorUserSchema()
vendor_users_schema = VendorUserSchema(many=True)
