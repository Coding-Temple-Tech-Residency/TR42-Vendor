from app.extensions import db
from app.blueprints.insurance.repositories.repository import InsuranceRepository


class InsuranceService:

    @staticmethod
    def get_all_insurances():
        return InsuranceRepository.get_all()

    @staticmethod
    def get_insurance(insurance_id):
        return InsuranceRepository.get_by_id(insurance_id)

    @staticmethod
    def create_insurance(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_insurance(insurance_id, data):
        insurance = InsuranceRepository.get_by_id(insurance_id)

        if not insurance:
            return None

        for key, value in data.items():
            setattr(insurance, key, value)

        db.session.commit()
        return insurance

    @staticmethod
    def delete_insurance(insurance_id):
        insurance = InsuranceRepository.get_by_id(insurance_id)

        if not insurance:
            return None

        db.session.delete(insurance)
        db.session.commit()
        return insurance