from app.extensions import ma
from app.blueprints.contractor_performance import ContractorPerformance


class ContractorPerformanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContractorPerformance
        load_instance = True


contractor_performance_schema = ContractorPerformanceSchema()
contractor_performances_schema = ContractorPerformanceSchema(many=True)