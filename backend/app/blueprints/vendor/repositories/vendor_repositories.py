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
    def get_all_paginated(page: int = 1, per_page: int = 10):
        return db.paginate(select(Vendor), page=page, per_page=per_page)

    @staticmethod
    def get_by_company_name(company_name: str):
        try:
            logger.debug("Fetching vendor by company name")
            return db.session.scalar(
                select(Vendor).where(Vendor.company_name == company_name)
            )
        except Exception:
            logger.exception("Failed to fetch vendor by name")
            raise

    @staticmethod
    def get_by_company_email(company_email: str):
        try:
            logger.debug("Fetching vendor by company name")
            return db.session.scalar(
                select(Vendor).where(Vendor.company_email == company_email)
            )
        except Exception:
            logger.exception("Failed to fetch vendor by email")
            raise

    @staticmethod
    def get_by_id(vendor_id: str):
        try:
            logger.debug("Fetching vendor by vendor_id")
            return db.session.scalar(select(Vendor).where(Vendor.id == vendor_id))
        except Exception:
            logger.exception("Failed to fetch by vendor_id")
            raise

    @staticmethod
    def create(vendor: Vendor):
        try:
            logger.debug("Adding vendor to session")
            db.session.add(vendor)
            return vendor
        except Exception:
            logger.exception("Failed to add vendor to session")
            raise

    @staticmethod
    def delete(vendor: Vendor):
        db.session.delete(vendor)
