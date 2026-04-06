import logging
from sqlalchemy import select

from app.extensions import db
from app.blueprints.vendor.model import Vendor

logger = logging.getLogger(__name__)


class VendorRepository:

    @staticmethod
    def get_all():
        try:
            logger.debug("Fetching all vendors from database")
            return db.session.scalars(select(Vendor)).all()
        except Exception:
            logger.exception("Failed to fetch vendors from database")
            raise

    @staticmethod
    def get_by_company_name(company_name: str):
        try:
            logger.debug("Fetching vendor by name: %s", company_name)
            return db.session.scalar(
                select(Vendor).where(Vendor.company_name == company_name)
            )
        except Exception:
            logger.exception("Failed to fetch vendor by name: %s", company_name)
            raise

    @staticmethod
    def create(vendor: Vendor) -> Vendor:
        try:
            logger.debug("Adding vendor to session: %s", vendor.company_name)
            db.session.add(vendor)
            return vendor
        except Exception:
            logger.exception("Failed to add vendor to session")
            raise
