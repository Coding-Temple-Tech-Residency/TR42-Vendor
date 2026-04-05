from app.extensions import ma
from app.models.work_order import Rating


class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating
        load_instance = True


rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)