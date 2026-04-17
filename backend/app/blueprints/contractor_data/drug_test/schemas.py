from app.extensions import ma
from marshmallow import fields
from app.blueprints.contractor_data.drug_test.model import DrugTest


class DrugTestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DrugTest
        load_instance = False
        include_fk = True
        include_relationships = False


class DrugTestCreateSchema(ma.Schema):
    drug_test_passed = fields.Boolean(required=True)
    drug_test_date = fields.DateTime(required=False, allow_none=True)


drug_test_schema = DrugTestSchema()
drug_tests_schema = DrugTestSchema(many=True)
drug_test_create_schema = DrugTestCreateSchema()
