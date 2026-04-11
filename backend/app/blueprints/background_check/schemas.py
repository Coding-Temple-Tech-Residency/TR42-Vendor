from app.extensions import ma
from app.blueprints.background_check.model import BackgroundCheck
from marshmallow import fields

class BackgroundCheckSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BackgroundCheck
        load_instance = True

    background_check_id = fields.String(dump_only=True)

    background_check_passed = fields.Boolean(required=True)

    background_check_date = fields.DateTime(required=True)
    
    background_check_provider = fields.String(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    
    
    
background_check_schema = BackgroundCheckSchema()
background_checks_schema = BackgroundCheckSchema(many=True)