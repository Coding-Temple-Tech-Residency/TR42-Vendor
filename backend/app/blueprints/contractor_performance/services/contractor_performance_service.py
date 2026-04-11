from app.extensions import db
from app.blueprints.contractor_performance.repositories.repository import ContractorPerformanceRepository 


class ContractorPerformanceService:

    @staticmethod
    def get_all_contractor_performances():
        return ContractorPerformanceRepository.get_all()

    @staticmethod
    def get_contractor_performance(contractor_performance_id):
        return ContractorPerformanceRepository.get_by_id(contractor_performance_id)

    @staticmethod
    def create_contractor_performance(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_contractor_performance(contractor_performance_id, data):
        contractor_performance = ContractorPerformanceRepository.get_by_id(contractor_performance_id)

        if not contractor_performance:
            return None

        for key, value in data.items():
            setattr(contractor_performance, key, value)

        db.session.commit()
        return contractor_performance

    @staticmethod
    def delete_contractor_performance(contractor_performance_id):
        contractor_performance = ContractorPerformanceRepository.get_by_id(contractor_performance_id)

        if not contractor_performance:
            return None

        db.session.delete(contractor_performance)
        db.session.commit()
        return contractor_performance
