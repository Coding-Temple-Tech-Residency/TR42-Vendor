import logging
from marshmallow import ValidationError

from app.extensions import db
from app.blueprints.contractor.repositories.contractor_repositories import (
    ContractorRepository,
)
from app.blueprints.contractor_data.insurance.model import Insurance
from app.blueprints.contractor_data.insurance.repositories.insurance_repositories import (
    InsuranceRepository,
)

logger = logging.getLogger(__name__)


class InsuranceService:

    @staticmethod
    def create_insurance(
        contractor_id: str,
        validated_data: dict,
        created_by: str | None,
        updated_by: str | None,
    ):
        try:
            logger.debug("Creating insurance")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            insurance = Insurance(
                contractor_id=contractor_id,
                insurance_type=validated_data["insurance_type"],
                policy_number=validated_data["policy_number"],
                provider_name=validated_data["provider_name"],
                provider_phone=validated_data["provider_phone"],
                coverage_amount=validated_data.get("coverage_amount"),
                deductible=validated_data.get("deductible"),
                effective_date=validated_data.get("effective_date"),
                expiration_date=validated_data.get("expiration_date"),
                insurance_document_url=validated_data.get("insurance_document_url"),
                insurance_verified=validated_data.get("insurance_verified", False),
                additional_insurance_required=validated_data.get(
                    "additional_insurance_required",
                    False,
                ),
                additional_insured_certificate_url=validated_data.get(
                    "additional_insured_certificate_url"
                ),
                created_by=created_by,
                updated_by=updated_by,
            )

            InsuranceRepository.create(insurance)

            db.session.commit()
            db.session.refresh(insurance)

            logger.info("Insurance created successfully")
            return insurance

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create insurance")
            raise

    @staticmethod
    def get_insurances_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching insurances by contractor_id")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            return InsuranceRepository.get_by_contractor(contractor_id)

        except ValidationError:
            raise
        except Exception:
            logger.exception("Failed to fetch insurances by contractor_id")
            raise

    @staticmethod
    def get_insurance(insurance_id: str):
        try:
            logger.debug("Fetching insurance by id")

            insurance = InsuranceRepository.get_by_id(insurance_id)
            if not insurance:
                return None

            return insurance

        except Exception:
            logger.exception("Failed to fetch insurance by id")
            raise

    @staticmethod
    def update_insurance(
        insurance_id: str,
        validated_data: dict,
        updated_by: str | None,
    ):
        try:
            logger.debug("Updating insurance")

            insurance = InsuranceRepository.get_by_id(insurance_id)
            if not insurance:
                return None

            for key, value in validated_data.items():
                setattr(insurance, key, value)

            insurance.updated_by = updated_by

            InsuranceRepository.update(insurance)

            db.session.commit()
            db.session.refresh(insurance)

            logger.info("Insurance updated successfully")
            return insurance

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to update insurance")
            raise

    @staticmethod
    def delete_insurance(insurance_id: str):
        try:
            logger.debug("Deleting insurance")

            insurance = InsuranceRepository.get_by_id(insurance_id)
            if not insurance:
                return None

            InsuranceRepository.delete(insurance)
            db.session.commit()

            logger.info("Insurance deleted successfully")
            return True

        except Exception:
            db.session.rollback()
            logger.exception("Failed to delete insurance")
            raise
