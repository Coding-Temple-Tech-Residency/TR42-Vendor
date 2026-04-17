import logging
from sqlalchemy import select
from app.extensions import db
from app.blueprints.contractor_data.license.model import License

logger = logging.getLogger(__name__)


class LicenseRepository:

    @staticmethod
    def get_by_id(license_id: str):
        try:
            logger.debug("Fetching license by id")
            return db.session.scalar(select(License).where(License.id == license_id))
        except Exception:
            logger.exception("Failed to fetch license by id")
            raise

    @staticmethod
    def get_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching licenses by contractor_id")
            return db.session.scalars(
                select(License).where(License.contractor_id == contractor_id)
            ).all()
        except Exception:
            logger.exception("Failed to fetch licenses by contractor_id")
            raise

    @staticmethod
    def create(license_record: License):
        try:
            logger.debug("Creating license")
            db.session.add(license_record)
            return license_record
        except Exception:
            logger.exception("Failed to create license")
            raise

    @staticmethod
    def update(license_record: License):
        try:
            logger.debug("Updating license")
            db.session.add(license_record)
            return license_record
        except Exception:
            logger.exception("Failed to update license")
            raise

    @staticmethod
    def delete(license_record: License):
        try:
            logger.debug("Deleting license")
            db.session.delete(license_record)
        except Exception:
            logger.exception("Failed to delete license")
            raise
