import logging
from sqlalchemy import select
from app.extensions import db
from app.blueprints.contractor_data.biometric_data.model import BiometricData

logger = logging.getLogger(__name__)


class BiometricDataRepository:

    @staticmethod
    def get_by_id(biometric_data_id: str):
        try:
            logger.debug("Fetching biometric data by id")
            return db.session.scalar(
                select(BiometricData).where(BiometricData.id == biometric_data_id)
            )
        except Exception:
            logger.exception("Failed to fetch biometric data by id")
            raise

    @staticmethod
    def get_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching biometric data by contractor_id")
            return db.session.scalars(
                select(BiometricData).where(
                    BiometricData.contractor_id == contractor_id
                )
            ).all()
        except Exception:
            logger.exception("Failed to fetch biometric data by contractor_id")
            raise

    @staticmethod
    def update(biometric_data: BiometricData):
        try:
            logger.debug("Updating biometric data")
            db.session.add(biometric_data)
            return biometric_data
        except Exception:
            logger.exception("Failed to update biometric data")
            raise

    @staticmethod
    def create(biometric_data: BiometricData):
        try:
            logger.debug("Creating biometric data")
            db.session.add(biometric_data)
            return biometric_data
        except Exception:
            logger.exception("Failed to create biometric data")
            raise

    @staticmethod
    def delete(biometric_data: BiometricData):
        try:
            logger.debug("Deleting biometric data")
            db.session.delete(biometric_data)
        except Exception:
            logger.exception("Failed to delete biometric data")
            raise
