from app.extensions import ma
from marshmallow import fields
from app.blueprints.contractor_data.license.model import License


class LicenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = License
        load_instance = False
        include_fk = True
        include_relationships = False


class LicenseCreateSchema(ma.Schema):
    license_type = fields.String(required=True)
    license_number = fields.String(required=True)
    license_state = fields.String(required=True)
    license_expiration_date = fields.Date(required=True)
    license_document_url = fields.String(required=False, allow_none=True)
    license_verified = fields.Boolean(required=False)
    license_verified_by = fields.String(required=False, allow_none=True)
    license_verified_at = fields.DateTime(required=False, allow_none=True)


license_schema = LicenseSchema()
licenses_schema = LicenseSchema(many=True)
license_create_schema = LicenseCreateSchema()
