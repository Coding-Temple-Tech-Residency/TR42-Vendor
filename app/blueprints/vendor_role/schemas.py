from app.extensions import ma
from .model import VendorRole

class VendorRoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VendorRole
        load_instance = True

vendor_role_schema = VendorRoleSchema()
vendor_roles_schema = VendorRoleSchema(many=True)
