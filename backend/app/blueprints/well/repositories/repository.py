from app.blueprints.well.model import Well
from app.extensions import db

class WellRepository:
    
    @staticmethod
    def get_all():
        return Well.query.all()
    
    @staticmethod
    def get_by_id(well_id):
        return Well.query.get(well_id)
    
    @staticmethod
    def create(well):
        db.session.add(well)
        db.session.commit()
        return well
    
    @staticmethod
    def update(well):
        db.session.commit()
        return well
    
    @staticmethod
    def delete(well):
        db.session.delete(well)
        db.session.commit()