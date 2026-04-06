from ..repositories import ContractorPerformanceRepository
from ..model import ContractorPerformance

class ContractorPerformanceService:
    
    @staticmethod
    def get_all_contractor_performances():
        return ContractorPerformanceRepository.get_all()
    
    @staticmethod
    def get_contractor_performance(contractor_performance_id):
        return ContractorPerformanceRepository.get_by_id(contractor_performance_id)
    
    @staticmethod
    def create_contractor_performance(data):
        new_contractor_performance = ContractorPerformance(**data)
        return ContractorPerformanceRepository.create(new_contractor_performance)
    
    @staticmethod
    def update_contractor_performance(contractor_performance_id, data):
        contractor_performance = ContractorPerformanceRepository.get_by_id(contractor_performance_id)
        if not contractor_performance:
            return None
        for key, value in data.items():
            setattr(contractor_performance, key, value)
        return ContractorPerformanceRepository.update(contractor_performance)
    
    @staticmethod
    def delete_contractor_performance(contractor_performance_id):
        contractor_performance = ContractorPerformanceRepository.get_by_id(contractor_performance_id)
        if not contractor_performance:
            return None
        return ContractorPerformanceRepository.delete(contractor_performance)