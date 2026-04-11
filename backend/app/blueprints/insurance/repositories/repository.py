from app.blueprints.insurance.model import Insurance
from app.extensions import db

class InsuranceRepository:
    
    @staticmethod
    def get_all():
        return Insurance.query.all()
    
    @staticmethod
    def get_by_id(insurance_id):
        return Insurance.query.get(insurance_id)
    
    @staticmethod
    def create(insurance):
        db.session.add(insurance)
        db.session.commit()
        return insurance
    
    @staticmethod
    def update(insurance):
        db.session.commit()
        return insurance
    
    @staticmethod
    def delete(insurance):
        db.session.delete(insurance)
        db.session.commit()