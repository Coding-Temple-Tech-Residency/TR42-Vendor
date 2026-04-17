import logging
from marshmallow import ValidationError

from app.extensions import db
from app.blueprints.contractor.repositories.contractor_repositories import (
    ContractorRepository,
)
from app.blueprints.contractor_data.certification.model import Certification
from app.blueprints.contractor_data.certification.repositories.certification_repositories import (
    CertificationRepository,
)

logger = logging.getLogger(__name__)


class CertificationService:

    @staticmethod
    def create_certification(
        contractor_id: str,
        validated_data: dict,
        created_by: str | None,
        updated_by: str | None,
    ):
        try:
            logger.debug("Creating certification")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            certification = Certification(
                contractor_id=contractor_id,
                certification_name=validated_data.get("certification_name"),
                certifying_body=validated_data.get("certifying_body"),
                certification_number=validated_data["certification_number"],
                issue_date=validated_data["issue_date"],
                expiration_date=validated_data.get("expiration_date"),
                certification_document_url=validated_data.get(
                    "certification_document_url"
                ),
                certification_verified=validated_data.get(
                    "certification_verified",
                    False,
                ),
                created_by=created_by,
                updated_by=updated_by,
            )

            CertificationRepository.create(certification)

            db.session.commit()
            db.session.refresh(certification)

            logger.info("Certification created successfully")
            return certification

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create certification")
            raise

    @staticmethod
    def get_certifications_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching certifications by contractor_id")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            return CertificationRepository.get_by_contractor(contractor_id)

        except ValidationError:
            raise
        except Exception:
            logger.exception("Failed to fetch certifications by contractor_id")
            raise

    @staticmethod
    def get_certification(certification_id: str):
        try:
            logger.debug("Fetching certification by id")

            certification = CertificationRepository.get_by_id(certification_id)
            if not certification:
                return None

            return certification

        except Exception:
            logger.exception("Failed to fetch certification by id")
            raise

    @staticmethod
    def update_certification(
        certification_id: str,
        validated_data: dict,
        updated_by: str | None,
    ):
        try:
            logger.debug("Updating certification")

            certification = CertificationRepository.get_by_id(certification_id)
            if not certification:
                return None

            for key, value in validated_data.items():
                setattr(certification, key, value)

            certification.updated_by = updated_by

            CertificationRepository.update(certification)

            db.session.commit()
            db.session.refresh(certification)

            logger.info("Certification updated successfully")
            return certification

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to update certification")
            raise

    @staticmethod
    def delete_certification(certification_id: str):
        try:
            logger.debug("Deleting certification")

            certification = CertificationRepository.get_by_id(certification_id)
            if not certification:
                return None

            CertificationRepository.delete(certification)
            db.session.commit()

            logger.info("Certification deleted successfully")
            return True

        except Exception:
            db.session.rollback()
            logger.exception("Failed to delete certification")
            raise
