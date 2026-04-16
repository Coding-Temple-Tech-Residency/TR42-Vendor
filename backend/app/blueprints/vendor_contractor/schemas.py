from app.extensions import ma
from marshmallow import fields
from app.blueprints.vendor_contractor.model import (
    VendorContractor,
    VendorContractorRole,
)


class VendorContractorSchema(ma.SQLAlchemyAutoSchema):
    vendor_contractor_role = fields.Enum(VendorContractorRole, by_value=True)

    class Meta:
        model = VendorContractor
        load_instance = False
        include_fk = True
        include_relationships = False


vendor_contractor_create_schema = VendorContractorSchema()
vendor_contractors_update_schema = VendorContractorSchema(many=True)
