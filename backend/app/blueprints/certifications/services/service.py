from app.extensions import db
from app.blueprints.certifications.repositories.repository import CertificationRepository


class CertificationService:

    @staticmethod
    def get_all_certifications():
        return CertificationRepository.get_all()

    @staticmethod
    def get_certification(certification_id):
        return CertificationRepository.get_by_id(certification_id)

    @staticmethod
    def create_certification(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_certification(certification_id, data):
        certification = CertificationRepository.get_by_id(certification_id)

        if not certification:
            return None

        for key, value in data.items():
            setattr(certification, key, value)

        db.session.commit()
        return certification

    @staticmethod
    def delete_certification(certification_id):
        certification = CertificationRepository.get_by_id(certification_id)

        if not certification:
            return None

        db.session.delete(certification)
        db.session.commit()
        return certification