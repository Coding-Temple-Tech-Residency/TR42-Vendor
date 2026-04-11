from app.extensions import ma
from app.blueprints.insurance.model import Insurance



class InsuranceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Insurance
        load_instance = True


insurance_schema = InsuranceSchema()
insurances_schema = InsuranceSchema(many=True)
