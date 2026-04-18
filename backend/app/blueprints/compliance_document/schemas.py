from app.extensions import ma
from .model import VendorUser


class VendorUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VendorUser
        load_instance = True


vendor_user_schema = VendorUserSchema()
vendor_users_schema = VendorUserSchema(many=True)