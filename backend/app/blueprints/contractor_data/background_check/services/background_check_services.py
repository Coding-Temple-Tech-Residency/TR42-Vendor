import logging
from marshmallow import ValidationError

from app.extensions import db
from app.blueprints.contractor.repositories.contractor_repositories import (
    ContractorRepository,
)
from app.blueprints.contractor_data.background_check.model import BackgroundCheck
from app.blueprints.contractor_data.background_check.repositories.background_check_repositories import (
    BackgroundCheckRepository,
)

logger = logging.getLogger(__name__)


class BackgroundCheckService:

    @staticmethod
    def create_background_check(
        contractor_id: str,
        validated_data: dict,
        created_by: str | None,
        updated_by: str | None,
    ):
        try:
            logger.debug("Creating background check")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            background_check = BackgroundCheck(
                contractor_id=contractor_id,
                background_check_passed=validated_data["background_check_passed"],
                background_check_date=validated_data.get("background_check_date"),
                background_check_provider=validated_data.get(
                    "background_check_provider"
                ),
                created_by=created_by,
                updated_by=updated_by,
            )

            BackgroundCheckRepository.create(background_check)

            db.session.commit()
            db.session.refresh(background_check)

            logger.info("Background check created successfully")
            return background_check

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create background check")
            raise

    @staticmethod
    def get_background_checks_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching background checks by contractor_id")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            return BackgroundCheckRepository.get_by_contractor(contractor_id)

        except ValidationError:
            raise
        except Exception:
            logger.exception("Failed to fetch background checks by contractor_id")
            raise

    @staticmethod
    def get_background_check(background_check_id: str):
        try:
            logger.debug("Fetching background check by id")

            background_check = BackgroundCheckRepository.get_by_id(background_check_id)
            if not background_check:
                return None

            return background_check

        except Exception:
            logger.exception("Failed to fetch background check by id")
            raise

    @staticmethod
    def delete_background_check(background_check_id: str):
        try:
            logger.debug("Deleting background check")

            background_check = BackgroundCheckRepository.get_by_id(background_check_id)
            if not background_check:
                return None

            BackgroundCheckRepository.delete(background_check)
            db.session.commit()

            logger.info("Background check deleted successfully")
            return True

        except Exception:
            db.session.rollback()
            logger.exception("Failed to delete background check")
            raise
