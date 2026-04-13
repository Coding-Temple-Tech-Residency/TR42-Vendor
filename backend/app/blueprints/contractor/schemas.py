from app.extensions import ma
from blueprints.contractor import Contractor


class ContractorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contractor
        load_instance = True


contractor_schema = ContractorSchema()
contractors_schema = ContractorSchema(many=True)