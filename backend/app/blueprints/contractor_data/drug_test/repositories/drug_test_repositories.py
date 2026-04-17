import logging
from sqlalchemy import select
from app.extensions import db
from app.blueprints.contractor_data.drug_test.model import DrugTest

logger = logging.getLogger(__name__)


class DrugTestRepository:

    @staticmethod
    def get_by_id(drug_test_id: str):
        try:
            logger.debug("Fetching drug test by id")
            return db.session.scalar(
                select(DrugTest).where(DrugTest.id == drug_test_id)
            )
        except Exception:
            logger.exception("Failed to fetch drug test by id")
            raise

    @staticmethod
    def get_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching drug tests by contractor_id")
            return db.session.scalars(
                select(DrugTest).where(DrugTest.contractor_id == contractor_id)
            ).all()
        except Exception:
            logger.exception("Failed to fetch drug tests by contractor_id")
            raise

    @staticmethod
    def create(drug_test: DrugTest):
        try:
            logger.debug("Creating drug test")
            db.session.add(drug_test)
            return drug_test
        except Exception:
            logger.exception("Failed to create drug test")
            raise

    @staticmethod
    def update(drug_test: DrugTest):
        try:
            logger.debug("Updating drug test")
            db.session.add(drug_test)
            return drug_test
        except Exception:
            logger.exception("Failed to update drug test")
            raise

    @staticmethod
    def delete(drug_test: DrugTest):
        try:
            logger.debug("Deleting drug test")
            db.session.delete(drug_test)
        except Exception:
            logger.exception("Failed to delete drug test")
            raise
