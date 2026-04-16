from sqlalchemy import select

from app.blueprints.contractor.model import Contractor
import logging
from app.extensions import db

logger = logging.getLogger(__name__)


class ContractorRepository:

    @staticmethod
    def get_all():
        try:
            logger.debug("Fetching all contractors from database")
            return db.session.scalars(select(Contractor)).all()
        except Exception:
            logger.exception("Failed to fetch contractors from database")
            raise

    @staticmethod
    def get_all_paginated(page: int = 1, per_page: int = 10):
        return db.paginate(select(Contractor), page=page, per_page=per_page)

    @staticmethod
    def get_by_id(contractor_id: str):
        try:
            logger.debug("Fetching vendor by contractor_id")
            return db.session.scalar(
                select(Contractor).where(Contractor.id == contractor_id)
            )
        except Exception:
            logger.exception("Failed to fetch by contractor_id")
            raise

    @staticmethod
    def create(contractor: Contractor):
        try:
            logger.debug("Adding contractor to session")
            db.session.add(contractor)
            return contractor
        except Exception:
            logger.exception("Failed to add contractor to session")
            raise

    @staticmethod
    def delete(contractor):
        db.session.delete(contractor)
