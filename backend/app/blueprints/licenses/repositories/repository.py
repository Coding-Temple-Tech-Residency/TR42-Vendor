from app.blueprints.licenses.model import License
from app.extensions import db

class LicenseRepository:
    
    @staticmethod
    def get_all():
        return License.query.all()
    
    @staticmethod
    def get_by_id(license_id):
        return License.query.get(license_id)
    
    @staticmethod
    def create(license):
        db.session.add(license)
        db.session.commit()
        return license
    
    @staticmethod
    def update(license):
        db.session.commit()
        return license
    
    @staticmethod
    def delete(license):
        db.session.delete(license)
        db.session.commit()