from app.extensions import ma
from marshmallow import fields
from app.blueprints.contractor_data.insurance.model import Insurance


class InsuranceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Insurance
        load_instance = False
        include_fk = True
        include_relationships = False


class InsuranceCreateSchema(ma.Schema):
    insurance_type = fields.String(required=True)
    policy_number = fields.String(required=True)
    provider_name = fields.String(required=True)
    provider_phone = fields.String(required=True)
    coverage_amount = fields.Decimal(required=False, allow_none=True, as_string=True)
    deductible = fields.Decimal(required=False, allow_none=True, as_string=True)
    effective_date = fields.Date(required=False, allow_none=True)
    expiration_date = fields.Date(required=False, allow_none=True)
    insurance_document_url = fields.String(required=False, allow_none=True)
    insurance_verified = fields.Boolean(required=False)
    additional_insurance_required = fields.Boolean(required=False)
    additional_insured_certificate_url = fields.String(required=False, allow_none=True)


insurance_schema = InsuranceSchema()
insurances_schema = InsuranceSchema(many=True)
insurance_create_schema = InsuranceCreateSchema()
