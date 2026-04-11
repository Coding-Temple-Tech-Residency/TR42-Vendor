from app.extensions import db
from app.blueprints.background_check.repositories.repository import BackgroundCheckRepository


class BackgroundCheckService:

    @staticmethod
    def get_all_drug_tests():
        return BackgroundCheckRepository.get_all()

    @staticmethod
    def get_drug_test(background_check_id):
        return BackgroundCheckRepository.get_by_id(background_check_id)

    @staticmethod
    def create_drug_test(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_drug_test(background_check_id, data):
        background_check = BackgroundCheckRepository.get_by_id(background_check_id)

        if not background_check:
            return None

        for key, value in data.items():
            setattr(background_check, key, value)

        db.session.commit()
        return background_check

    @staticmethod
    def delete_drug_test(background_check_id):
        background_check = BackgroundCheckRepository.get_by_id(background_check_id)

        if not background_check:
            return None

        db.session.delete(background_check)
        db.session.commit()
        return background_check