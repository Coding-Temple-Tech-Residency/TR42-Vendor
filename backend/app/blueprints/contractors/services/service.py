from .repository import ContractorRepository
from models import Contractor

class ContractorService:

    @staticmethod
    def get_all_contractors():
        return ContractorRepository.get_all()

    @staticmethod
    def get_contractor(contractor_id):
        return ContractorRepository.get_by_id(contractor_id)

    @staticmethod
    def create_contractor(data):
        contractor = Contractor(**data)
        return ContractorRepository.create(contractor)

    @staticmethod
    def update_contractor(contractor, data):
        for key, value in data.items():
            setattr(contractor, key, value)
        ContractorRepository.update()
        return contractor

    @staticmethod
    def delete_contractor(contractor):
        ContractorRepository.delete(contractor)
        return True