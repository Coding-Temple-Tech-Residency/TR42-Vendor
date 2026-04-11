from app.extensions import ma
from app.blueprints.contractor_performance.model import ContractorPerformance
from marshmallow import fields, validate

class ContractorPerformanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContractorPerformance
        load_instance = True

    rating_id = fields.String(dump_only=True)

    contractor_id = fields.String(required=True)

    rating = fields.Integer(
        required=True,
        validate=validate.Range(min=1, max=5)
    )

    comments = fields.String(required=False, allow_none=True)
    
    ticket_id = fields.String(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    
    
    
contractor_performance_schema = ContractorPerformanceSchema()
contractor_performances_schema = ContractorPerformanceSchema(many=True)