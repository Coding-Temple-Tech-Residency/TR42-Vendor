import logging
from sqlalchemy import select
from app.extensions import db
from app.blueprints.contractor_data.insurance.model import Insurance

logger = logging.getLogger(__name__)


class InsuranceRepository:

    @staticmethod
    def get_by_id(insurance_id: str):
        try:
            logger.debug("Fetching insurance by id")
            return db.session.scalar(
                select(Insurance).where(Insurance.id == insurance_id)
            )
        except Exception:
            logger.exception("Failed to fetch insurance by id")
            raise

    @staticmethod
    def get_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching insurances by contractor_id")
            return db.session.scalars(
                select(Insurance).where(Insurance.contractor_id == contractor_id)
            ).all()
        except Exception:
            logger.exception("Failed to fetch insurances by contractor_id")
            raise

    @staticmethod
    def create(insurance: Insurance):
        try:
            logger.debug("Creating insurance")
            db.session.add(insurance)
            return insurance
        except Exception:
            logger.exception("Failed to create insurance")
            raise

    @staticmethod
    def update(insurance: Insurance):
        try:
            logger.debug("Updating insurance")
            db.session.add(insurance)
            return insurance
        except Exception:
            logger.exception("Failed to update insurance")
            raise

    @staticmethod
    def delete(insurance: Insurance):
        try:
            logger.debug("Deleting insurance")
            db.session.delete(insurance)
        except Exception:
            logger.exception("Failed to delete insurance")
            raise
