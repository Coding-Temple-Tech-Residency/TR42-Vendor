from app.extensions import ma
from app.blueprints.well.model import Well



class WellSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Well
        load_instance = True


well_schema = WellSchema()
wells_schema = WellSchema(many=True)
