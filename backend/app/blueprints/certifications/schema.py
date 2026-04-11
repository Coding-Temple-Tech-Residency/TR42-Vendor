from app.extensions import ma
from app.blueprints.certifications.model import Certification
from marshmallow import fields

class CertificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Certification
        load_instance = True

    certification_id = fields.String(dump_only=True)

    certification_name = fields.String(required=True)
    
    certifying_body = fields.String(required=True)
    
    certification_number = fields.Integer(required=True)
    
    issue_date = fields.DateTime(required=True)
    
    expiration_date = fields.DateTime()
    
    certification_document_url = fields.String()
    
    certification_verified = fields.Boolean()

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    
    
    
certification_schema = CertificationSchema()
certifications_schema = CertificationSchema(many=True)