from sqlalchemy import select
from app.extensions import db
from app.blueprints.vendor_user.model import VendorUser
import logging


logger = logging.getLogger(__name__)


class VendorUserRepository:

    @staticmethod
    def get_all():
        try:
            logger.debug("Fetching all vendor users from database")
            return VendorUser.query.all()
        except Exception:
            logger.exception("Failed to fetch vendor users")
            raise

    @staticmethod
    def get_by_user_and_vendor(user_id: str, vendor_id: str) -> VendorUser | None:
        try:
            logger.debug(
                "Fetching vendor link for user_id=%s and vendor_id=%s",
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
                "Failed to fetch vendor link for user_id=%s and vendor_id=%s",
                user_id,
                vendor_id,
            )
            raise

    @staticmethod
    def create(vendor_user: VendorUser):
        try:
            logger.debug("Creating vendor user with ID: %s", vendor_user.id)
            db.session.add(vendor_user)
            return vendor_user
        except Exception:
            logger.exception("Failed to create vendor user: %s", vendor_user.id)
            raise
from sqlalchemy import select
from app.extensions import db
from app.blueprints.vendor_user.model import VendorUser
import logging

logger = logging.getLogger(__name__)


class VendorUserRepository:

    @staticmethod
    def get_all():
        try:
            logger.debug("Fetching all vendor users from database")
            return VendorUser.query.all()
        except Exception:
            logger.exception("Failed to fetch vendor users")
            raise

    @staticmethod
    def get_by_user_and_vendor(user_id: str, vendor_id: str) -> VendorUser | None:
        try:
            logger.debug(
                "Fetching vendor link for user_id=%s and vendor_id=%s",
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
                "Failed to fetch vendor link for user_id=%s and vendor_id=%s",
                user_id,
                vendor_id,
            )
            raise

    @staticmethod
    def create(vendor_user: VendorUser):
        try:
            logger.debug("Creating vendor user with ID: %s", vendor_user.id)
            db.session.add(vendor_user)
            return vendor_user
        except Exception:
            logger.exception("Failed to create vendor user: %s", vendor_user.id)
            raise

    @staticmethod
    def get_by_id(vendor_user_id):
        try:
            logger.debug("Fetching vendor user by ID: %s", vendor_user_id)
            return db.session.get(VendorUser, vendor_user_id)
        except Exception:
            logger.exception("Failed to fetch vendor user by ID: %s", vendor_user_id)
            raise

    @staticmethod
    def get_by_vendor_id(vendor_id):
        try:
            logger.debug("Fetching vendor users for vendor_id: %s", vendor_id)
            return VendorUser.query.filter_by(vendor_id=vendor_id).all()
        except Exception:
            logger.exception("Failed to fetch vendor users by vendor_id: %s", vendor_id)
            raise

    @staticmethod
    def get_by_user_id(user_id):
        try:
            logger.debug("Fetching vendor users for user_id: %s", user_id)
            return VendorUser.query.filter_by(user_id=user_id).all()
        except Exception:
            logger.exception("Failed to fetch vendor users by user_id: %s", user_id)
            raise

    @staticmethod
    def update(vendor_user):
        try:
            logger.debug("Updating vendor user with ID: %s", vendor_user.id)
            return vendor_user
        except Exception:
            logger.exception("Failed to update vendor user: %s", vendor_user.id)
            raise

    @staticmethod
    def delete(vendor_user):
        try:
            logger.debug("Deleting vendor user with ID: %s", vendor_user.id)
            db.session.delete(vendor_user)
        except Exception:
            logger.exception("Failed to delete vendor user: %s", vendor_user.id)
            raise