from sqlalchemy import select

from app.blueprints.contractor.model import Contractor
from app.blueprints.vendor_contractor.model import VendorContractor
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
    def get_by_vendor_paginated(vendor_id: str, page: int = 1, per_page: int = 10):
        stmt = (
            select(Contractor)
            .join(Contractor.vendor_links)
            .where(VendorContractor.vendor_id == vendor_id)
        )
        return db.paginate(stmt, page=page, per_page=per_page)

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
