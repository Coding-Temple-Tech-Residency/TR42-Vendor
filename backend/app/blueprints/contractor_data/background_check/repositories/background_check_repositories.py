import logging
from sqlalchemy import select
from app.extensions import db
from app.blueprints.contractor_data.background_check.model import BackgroundCheck

logger = logging.getLogger(__name__)


class BackgroundCheckRepository:

    @staticmethod
    def get_by_id(background_check_id: str):
        try:
            logger.debug("Fetching background check by id")
            return db.session.scalar(
                select(BackgroundCheck).where(BackgroundCheck.id == background_check_id)
            )
        except Exception:
            logger.exception("Failed to fetch background check by id")
            raise

    @staticmethod
    def update(background_check: BackgroundCheck):
        try:
            logger.debug("Updating background check")
            db.session.add(background_check)
            return background_check
        except Exception:
            logger.exception("Failed to update background check")
            raise

    @staticmethod
    def get_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching background checks by contractor_id")
            return db.session.scalars(
                select(BackgroundCheck).where(
                    BackgroundCheck.contractor_id == contractor_id
                )
            ).all()
        except Exception:
            logger.exception("Failed to fetch background checks by contractor_id")
            raise

    @staticmethod
    def create(background_check: BackgroundCheck):
        try:
            logger.debug("Creating background check")
            db.session.add(background_check)
            return background_check
        except Exception:
            logger.exception("Failed to create background check")
            raise

    @staticmethod
    def delete(background_check: BackgroundCheck):
        try:
            logger.debug("Deleting background check")
            db.session.delete(background_check)
        except Exception:
            logger.exception("Failed to delete background check")
            raise
