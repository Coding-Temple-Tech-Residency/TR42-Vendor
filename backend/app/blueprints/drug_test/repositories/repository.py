from app.blueprints.drug_test.model import DrugTest
from app.extensions import db

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