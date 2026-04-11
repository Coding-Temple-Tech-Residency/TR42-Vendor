from app.blueprints.background_check.model import BackgroundCheck
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