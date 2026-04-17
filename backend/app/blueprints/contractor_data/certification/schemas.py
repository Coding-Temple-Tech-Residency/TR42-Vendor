from app.extensions import ma
from marshmallow import fields
from app.blueprints.contractor_data.certification.model import Certification


class CertificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Certification
        load_instance = False
        include_fk = True
        include_relationships = False


class CertificationCreateSchema(ma.Schema):
    certification_name = fields.String(required=False, allow_none=True)
    certifying_body = fields.String(required=False, allow_none=True)

    certification_number = fields.String(required=True)

    issue_date = fields.DateTime(required=True)
    expiration_date = fields.DateTime(required=False, allow_none=True)

    certification_document_url = fields.String(required=False, allow_none=True)

    certification_verified = fields.Boolean(required=False)


certification_schema = CertificationSchema()
certifications_schema = CertificationSchema(many=True)
certification_create_schema = CertificationCreateSchema()
