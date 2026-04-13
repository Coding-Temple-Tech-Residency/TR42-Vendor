from app.blueprints.documents.model import BackgroundCheck, DrugTest, ComplianceDocument
from app.extensions import db

class BackgroundCheckRepository:

    @staticmethod
    def get_all():
        return BackgroundCheck.query.all()
    
    @staticmethod
    def get_by_id(background_check_id):
        return BackgroundCheck.query.get(background_check_id)
    
    @staticmethod
    def create(background_check):
        db.session.add(background_check)
        db.session.commit()
        return background_check
    
    @staticmethod
    def update(background_check):
        db.session.commit()
        return background_check
    
    @staticmethod
    def delete(background_check):
        db.session.delete(background_check)
        db.session.commit()
        
        
class ComplianceDocumentRepository:
    
    @staticmethod
    def get_all():
        return ComplianceDocument.query.all()
    
    @staticmethod
    def get_by_id(compliance_document_id):
        return ComplianceDocument.query.get(compliance_document_id)
    
    @staticmethod
    def create(compliance_document):
        db.session.add(compliance_document)
        db.session.commit()
        return compliance_document
    
    @staticmethod
    def update(compliance_document):
        db.session.commit()
        return compliance_document
    
    @staticmethod
    def delete(compliance_document):
        db.session.delete(compliance_document)
        db.session.commit()
        
class DrugTestRepository:

    @staticmethod
    def get_all():
        return DrugTest.query.all()
    
    @staticmethod
    def get_by_id(drug_test_id):
        return DrugTest.query.get(drug_test_id)
    
    @staticmethod
    def create(drug_test):
        db.session.add(drug_test)
        db.session.commit()
        return drug_test
    
    @staticmethod
    def update(drug_test):
        db.session.commit()
        return drug_test
    
    @staticmethod
    def delete(drug_test):
        db.session.delete(drug_test)
        db.session.commit()