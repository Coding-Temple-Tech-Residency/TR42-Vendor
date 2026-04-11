from app.blueprints.certifications.model import Certification
from app.extensions import db

class CertificationRepository:
    
    @staticmethod
    def get_all():
        return Certification.query.all()
    
    @staticmethod
    def get_by_id(certification_id):
        return Certification.query.get(certification_id)
    
    @staticmethod
    def create(certification):
        db.session.add(certification)
        db.session.commit()
        return certification
    
    @staticmethod
    def update(certification):
        db.session.commit()
        return certification
    
    @staticmethod
    def delete(certification):
        db.session.delete(certification)
        db.session.commit()