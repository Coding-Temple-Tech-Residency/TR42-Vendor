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
    def create(vendor_user: VendorUser):
        try:
            logger.debug(f"Creating vendor user with ID: {vendor_user.id}")
            db.session.add(vendor_user)
            return vendor_user
        except Exception:
            logger.exception(f"Failed to create vendor user: {vendor_user.id}")
            raise
