from app.extensions import ma
from app.blueprints.contractor.model import Contractor


class ContractorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contractor
        load_instance = True


contractor_schema = ContractorSchema()
contractors_schema = ContractorSchema(many=True)
