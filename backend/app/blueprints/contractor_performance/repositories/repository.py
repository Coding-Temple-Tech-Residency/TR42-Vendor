from ..model import ContractorPerformance, db

class ContractorPerformanceRepository:
    
    @staticmethod
    def get_all():
        return ContractorPerformance.query.all()
    
    @staticmethod
    def get_by_id(contractor_performance_id):
        return ContractorPerformance.query.get(contractor_performance_id)
    
    @staticmethod
    def create(contractor_performance):
        db.session.add(contractor_performance)
        db.session.commit()
        return contractor_performance
    
    @staticmethod
    def update(contractor_performance):
        db.session.commit()
        return contractor_performance
    
    @staticmethod
    def delete(contractor_performance):
        db.session.delete(contractor_performance)
        db.session.commit()