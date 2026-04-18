
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
    def get_all_by_user(user_id: str) -> list[VendorUser]:
        try:
            logger.debug("Fetching vendor links for user_id=%s", user_id)
            return db.session.scalars(
                select(VendorUser).where(VendorUser.user_id == user_id)
            ).all()
        except Exception:
            logger.exception("Failed to fetch vendor links for user_id=%s", user_id)
            raise

    @staticmethod
    def create(vendor_user: VendorUser):
        try:
            logger.debug("Creating vendor user with id")
            db.session.add(vendor_user)
            return vendor_user
        except Exception:
            logger.exception("Failed to create vendor user")
            raise
