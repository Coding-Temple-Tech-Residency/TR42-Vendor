import logging
from marshmallow import ValidationError

from app.extensions import db
from app.blueprints.contractor.repositories.contractor_repositories import (
    ContractorRepository,
)
from app.blueprints.contractor_data.license.model import License
from app.blueprints.contractor_data.license.repositories.license_repositories import (
    LicenseRepository,
)

logger = logging.getLogger(__name__)


class LicenseService:

    @staticmethod
    def create_license(
        contractor_id: str,
        validated_data: dict,
        created_by: str | None,
        updated_by: str | None,
    ):
        try:
            logger.debug("Creating license")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            license_record = License(
                contractor_id=contractor_id,
                license_type=validated_data["license_type"],
                license_number=validated_data["license_number"],
                license_state=validated_data["license_state"],
                license_expiration_date=validated_data["license_expiration_date"],
                license_document_url=validated_data.get("license_document_url"),
                license_verified=validated_data.get("license_verified", False),
                license_verified_by=validated_data.get("license_verified_by"),
                license_verified_at=validated_data.get("license_verified_at"),
                created_by=created_by,
                updated_by=updated_by,
            )

            LicenseRepository.create(license_record)

            db.session.commit()
            db.session.refresh(license_record)

            logger.info("License created successfully")
            return license_record

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create license")
            raise

    @staticmethod
    def get_licenses_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching licenses by contractor_id")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            return LicenseRepository.get_by_contractor(contractor_id)

        except ValidationError:
            raise
        except Exception:
            logger.exception("Failed to fetch licenses by contractor_id")
            raise

    @staticmethod
    def get_license(license_id: str):
        try:
            logger.debug("Fetching license by id")

            license_record = LicenseRepository.get_by_id(license_id)
            if not license_record:
                return None

            return license_record

        except Exception:
            logger.exception("Failed to fetch license by id")
            raise

    @staticmethod
    def update_license(
        license_id: str,
        validated_data: dict,
        updated_by: str | None,
    ):
        try:
            logger.debug("Updating license")

            license_record = LicenseRepository.get_by_id(license_id)
            if not license_record:
                return None

            for key, value in validated_data.items():
                setattr(license_record, key, value)

            license_record.updated_by = updated_by

            LicenseRepository.update(license_record)

            db.session.commit()
            db.session.refresh(license_record)

            logger.info("License updated successfully")
            return license_record

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to update license")
            raise

    @staticmethod
    def delete_license(license_id: str):
        try:
            logger.debug("Deleting license")

            license_record = LicenseRepository.get_by_id(license_id)
            if not license_record:
                return None

            LicenseRepository.delete(license_record)
            db.session.commit()

            logger.info("License deleted successfully")
            return True

        except Exception:
            db.session.rollback()
            logger.exception("Failed to delete license")
            raise
