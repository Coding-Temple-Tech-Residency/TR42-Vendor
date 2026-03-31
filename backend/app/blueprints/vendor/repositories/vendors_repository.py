import logging
from app.extensions import db
from app.blueprints.vendors.model import Vendor

logger = logging.getLogger(__name__)


class VendorRepository:

    @staticmethod
    def get_all():
        try:
            logger.debug("Fetching all vendors from database")
            return db.session.query(Vendor).all()
        except Exception:
            logger.exception("Failed to fetch vendors from database")
            raise

    @staticmethod
    def get_by_company_name(company_name: str):
        try:
            logger.debug(f"Fetching vendor by name: {company_name}")
            return db.session.query(Vendor).filter_by(company_name=company_name).first()
        except Exception:
            logger.exception(f"Failed to fetch vendor by name: {company_name}")
            raise

    @staticmethod
    def create(vendor: Vendor):
        try:
            logger.debug(f"Saving vendor to database: {vendor.company_name}")

            db.session.add(vendor)
            db.session.commit()

            return vendor

        except Exception:
            db.session.rollback()
            logger.exception("Failed to create vendor in database")
            raise
