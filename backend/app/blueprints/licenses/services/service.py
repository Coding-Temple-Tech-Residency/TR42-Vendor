from app.extensions import db
from app.blueprints.licenses.repositories.repository import LicenseRepository


class LicenseService:

    @staticmethod
    def get_all_licenses():
        return LicenseRepository.get_all()

    @staticmethod
    def get_license(license_id):
        return LicenseRepository.get_by_id(license_id)

    @staticmethod
    def create_license(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_license(license_id, data):
        license = LicenseRepository.get_by_id(license_id)

        if not license:
            return None

        for key, value in data.items():
            setattr(license, key, value)

        db.session.commit()
        return license

    @staticmethod
    def delete_license(license_id):
        license = LicenseRepository.get_by_id(license_id)

        if not license:
            return None

        db.session.delete(license)
        db.session.commit()
        return license