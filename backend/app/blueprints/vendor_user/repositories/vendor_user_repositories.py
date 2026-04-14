import logging
from sqlalchemy import select

from app.extensions import db
from app.blueprints.vendor_user.model import VendorUser

logger = logging.getLogger(__name__)


class VendorUserRepository:

    @staticmethod
    def get_all():
        try:
            logger.debug("Fetching all vendor users from database")
            return db.session.scalars(select(VendorUser)).all()
        except Exception:
            logger.exception("Failed to fetch vendor users")
            raise

    @staticmethod
    def get_by_user_and_vendor(user_id: str, vendor_id: str):
        try:
            logger.debug(
                "Fetching vendor_user for user_id=%s and vendor_id=%s",
                user_id,
                vendor_id,
            )
            return db.session.scalar(
                select(VendorUser).where(
                    VendorUser.user_id == user_id,
                    VendorUser.vendor_id == vendor_id,
                )
            )
        except Exception:
            logger.exception(
                "Failed to fetch vendor_user for user_id=%s and vendor_id=%s",
                user_id,
                vendor_id,
            )
            raise

    @staticmethod
    def get_by_id(vendor_user_id: str):
        try:
            logger.debug("Fetching vendor_user by ID: %s", vendor_user_id)
            return db.session.get(VendorUser, vendor_user_id)
        except Exception:
            logger.exception("Failed to fetch vendor_user by ID: %s", vendor_user_id)
            raise

    @staticmethod
    def get_by_vendor_id(vendor_id: str):
        try:
            logger.debug("Fetching vendor_users for vendor_id: %s", vendor_id)
            return db.session.scalars(
                select(VendorUser).where(VendorUser.vendor_id == vendor_id)
            ).all()
        except Exception:
            logger.exception("Failed to fetch vendor_users for vendor_id: %s", vendor_id)
            raise

    @staticmethod
    def get_by_user_id(user_id: str):
        try:
            logger.debug("Fetching vendor_users for user_id: %s", user_id)
            return db.session.scalars(
                select(VendorUser).where(VendorUser.user_id == user_id)
            ).all()
        except Exception:
            logger.exception("Failed to fetch vendor_users for user_id: %s", user_id)
            raise

    @staticmethod
    def create(vendor_user: VendorUser) -> VendorUser:
        try:
            logger.debug("Adding vendor_user to session: %s", vendor_user.id)
            db.session.add(vendor_user)
            return vendor_user
        except Exception:
            logger.exception("Failed to add vendor_user to session")
            raise

    @staticmethod
    def delete(vendor_user: VendorUser):
        try:
            logger.debug("Deleting vendor_user with ID: %s", vendor_user.id)
            db.session.delete(vendor_user)
        except Exception:
            logger.exception("Failed to delete vendor_user: %s", vendor_user.id)
            raise
