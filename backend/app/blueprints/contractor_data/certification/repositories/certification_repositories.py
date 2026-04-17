import logging
from sqlalchemy import select

from app.extensions import db
from app.blueprints.contractor_data.certification.model import Certification

logger = logging.getLogger(__name__)


class CertificationRepository:

    @staticmethod
    def get_by_id(certification_id: str):
        try:
            logger.debug("Fetching certification by id")
            return db.session.scalar(
                select(Certification).where(Certification.id == certification_id)
            )
        except Exception:
            logger.exception("Failed to fetch certification by id")
            raise

    @staticmethod
    def get_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching certifications by contractor_id")
            return db.session.scalars(
                select(Certification).where(
                    Certification.contractor_id == contractor_id
                )
            ).all()
        except Exception:
            logger.exception("Failed to fetch certifications by contractor_id")
            raise

    @staticmethod
    def create(certification: Certification):
        try:
            logger.debug("Creating certification")
            db.session.add(certification)
            return certification
        except Exception:
            logger.exception("Failed to create certification")
            raise

    @staticmethod
    def update(certification: Certification):
        try:
            logger.debug("Updating certification")
            db.session.add(certification)
            return certification
        except Exception:
            logger.exception("Failed to update certification")
            raise

    @staticmethod
    def delete(certification: Certification):
        try:
            logger.debug("Deleting certification")
            db.session.delete(certification)
        except Exception:
            logger.exception("Failed to delete certification")
            raise
