from app.extensions import db
from app.blueprints.drug_test.repositories.repository import DrugTestRepository


class DrugTestService:

    @staticmethod
    def get_all_drug_tests():
        return DrugTestRepository.get_all()

    @staticmethod
    def get_drug_test(drug_test_id):
        return DrugTestRepository.get_by_id(drug_test_id)

    @staticmethod
    def create_drug_test(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_drug_test(drug_test_id, data):
        drug_test = DrugTestRepository.get_by_id(drug_test_id)

        if not drug_test:
            return None

        for key, value in data.items():
            setattr(drug_test, key, value)

        db.session.commit()
        return drug_test

    @staticmethod
    def delete_drug_test(drug_test_id):
        drug_test = DrugTestRepository.get_by_id(drug_test_id)

        if not drug_test:
            return None

        db.session.delete(drug_test)
        db.session.commit()
        return drug_test