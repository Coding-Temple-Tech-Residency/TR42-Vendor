import base64
import logging
from marshmallow import ValidationError

from app.extensions import db
from app.blueprints.contractor.repositories.contractor_repositories import (
    ContractorRepository,
)
from app.blueprints.contractor_data.biometric_data.model import BiometricData
from app.blueprints.contractor_data.biometric_data.repositories.biometric_data_repositories import (
    BiometricDataRepository,
)

logger = logging.getLogger(__name__)


class BiometricDataService:

    @staticmethod
    def create_biometric_data(
        contractor_id: str,
        validated_data: dict,
        created_by: str | None,
        updated_by: str | None,
    ):
        try:
            logger.debug("Creating biometric data")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            biometric_enrollment_data = validated_data.get("biometric_enrollment_data")
            if biometric_enrollment_data is not None:
                try:
                    biometric_enrollment_data = base64.b64decode(
                        biometric_enrollment_data
                    )
                except Exception:
                    raise ValidationError(
                        {"biometric_enrollment_data": ["Invalid base64-encoded data."]}
                    )

            biometric_data = BiometricData(
                contractor_id=contractor_id,
                biometric_enrollment_data=biometric_enrollment_data,
                created_by=created_by,
                updated_by=updated_by,
            )

            BiometricDataRepository.create(biometric_data)

            db.session.commit()
            db.session.refresh(biometric_data)

            logger.info("Biometric data created successfully")
            return biometric_data

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create biometric data")
            raise

    @staticmethod
    def get_biometric_data_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching biometric data by contractor_id")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            return BiometricDataRepository.get_by_contractor(contractor_id)

        except ValidationError:
            raise
        except Exception:
            logger.exception("Failed to fetch biometric data by contractor_id")
            raise

    @staticmethod
    def update_biometric_data(
        biometric_data_id: str,
        validated_data: dict,
        updated_by: str | None,
    ):
        try:
            logger.debug("Updating biometric data")

            biometric_data = BiometricDataRepository.get_by_id(biometric_data_id)
            if not biometric_data:
                return None

            if "biometric_enrollment_data" in validated_data:
                biometric_enrollment_data = validated_data.get(
                    "biometric_enrollment_data"
                )

                if biometric_enrollment_data is not None:
                    try:
                        biometric_enrollment_data = base64.b64decode(
                            biometric_enrollment_data
                        )
                    except Exception:
                        raise ValidationError(
                            {
                                "biometric_enrollment_data": [
                                    "Invalid base64-encoded data."
                                ]
                            }
                        )

                biometric_data.biometric_enrollment_data = biometric_enrollment_data

            biometric_data.updated_by = updated_by

            BiometricDataRepository.update(biometric_data)

            db.session.commit()
            db.session.refresh(biometric_data)

            logger.info("Biometric data updated successfully")
            return biometric_data

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to update biometric data")
            raise

    @staticmethod
    def get_biometric_data(biometric_data_id: str):
        try:
            logger.debug("Fetching biometric data by id")

            biometric_data = BiometricDataRepository.get_by_id(biometric_data_id)
            if not biometric_data:
                return None

            return biometric_data

        except Exception:
            logger.exception("Failed to fetch biometric data by id")
            raise

    @staticmethod
    def delete_biometric_data(biometric_data_id: str):
        try:
            logger.debug("Deleting biometric data")

            biometric_data = BiometricDataRepository.get_by_id(biometric_data_id)
            if not biometric_data:
                return None

            BiometricDataRepository.delete(biometric_data)
            db.session.commit()

            logger.info("Biometric data deleted successfully")
            return True

        except Exception:
            db.session.rollback()
            logger.exception("Failed to delete biometric data")
            raise
