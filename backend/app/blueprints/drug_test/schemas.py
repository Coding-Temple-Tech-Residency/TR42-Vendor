from app.extensions import ma
from app.blueprints.drug_test.model import DrugTest
from marshmallow import fields

class DrugTestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DrugTest
        load_instance = True

    drug_test_id = fields.String(dump_only=True)

    drug_test_passed = fields.Boolean(required=True)
    
    drug_test_date = fields.DateTime(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    
    
    
drug_test_schema = DrugTestSchema()
drug_tests_schema = DrugTestSchema(many=True)