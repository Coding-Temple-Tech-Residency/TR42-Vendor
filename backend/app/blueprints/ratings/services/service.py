from .repository import RatingRepository
from models import Rating

class RatingService:
    
    @staticmethod
    def get_all_ratings():
        return RatingRepository.get_all()
    
    @staticmethod
    def get_rating(rating_id):
        return RatingRepository.get_by_id(rating_id)
    
    @staticmethod
    def create_rating(data):
        new_rating = Rating(**data)
        return RatingRepository.create(new_rating)
    
    @staticmethod
    def update_rating(rating_id, data):
        rating = RatingRepository.get_by_id(rating_id)
        if not rating:
            return None
        for key, value in data.items():
            setattr(rating, key, value)
        return RatingRepository.update(rating)
    
    @staticmethod
    def delete_rating(rating_id):
        rating = RatingRepository.get_by_id(rating_id)
        if not rating:
            return None
        return RatingRepository.delete(rating)