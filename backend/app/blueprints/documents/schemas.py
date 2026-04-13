from app.extensions import ma
from app.blueprints.documents.model import DrugTest, ComplianceDocument, BackgroundCheck

class DrugTestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DrugTest
        load_instance = True


drug_test_schema = DrugTestSchema()
drug_tests_schema = DrugTestSchema(many=True)

class ComplianceDocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ComplianceDocument
        load_instance = True


compliance_document_schema = ComplianceDocumentSchema()
compliance_documents_schema = ComplianceDocumentSchema(many=True)

class BackgroundCheckSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BackgroundCheck
        load_instance = True


background_check_schema = BackgroundCheckSchema()
background_checks_schema = BackgroundCheckSchema(many=True)

