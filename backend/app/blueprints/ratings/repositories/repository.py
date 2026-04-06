from ..model import Rating, db

class RatingRepository:
    
    @staticmethod
    def get_all():
        return Rating.query.all()
    
    @staticmethod
    def get_by_id(rating_id):
        return Rating.query.get(rating_id)
    
    @staticmethod
    def create(rating):
        db.session.add(rating)
        db.session.commit()
        return rating
    
    @staticmethod
    def update(rating):
        db.session.commit()
        return rating
    
    @staticmethod
    def delete(rating):
        db.session.delete(rating)
        db.session.commit()