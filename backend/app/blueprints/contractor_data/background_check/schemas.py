from app.extensions import ma
from marshmallow import fields
from app.blueprints.contractor_data.background_check.model import BackgroundCheck


class BackgroundCheckSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BackgroundCheck
        load_instance = False
        include_fk = True
        include_relationships = False


class BackgroundCheckCreateSchema(ma.Schema):
    background_check_passed = fields.Boolean(required=True)
    background_check_date = fields.Date(required=False, allow_none=True)
    background_check_provider = fields.String(required=False, allow_none=True)


background_check_schema = BackgroundCheckSchema()
background_checks_schema = BackgroundCheckSchema(many=True)
background_check_create_schema = BackgroundCheckCreateSchema()
