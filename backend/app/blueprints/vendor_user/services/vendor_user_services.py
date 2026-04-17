from app.extensions import db
from app.blueprints.vendor_user.model import VendorUser, VendorUserRole
from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
    VendorUserRepository,
)
import logging

logger = logging.getLogger(__name__)


class VendorUserService:

    @staticmethod
    def get_all_users():
        try:
            logger.debug("Retrieving all vendor users from service layer")
            return VendorUserRepository.get_all()
        except Exception:
            logger.exception("Failed to retrieve vendor users in service layer")
            raise

    @staticmethod
    def add_user_to_vendor(data):
        try:
            logger.debug("Creating vendor user in service layer with data: %s", data)

            created_by = data.get("created_by") or data.get("created_by_user_id")
            updated_by = data.get("updated_by") or data.get("updated_by_user_id")

            vendor_user = VendorUser(
                user_id=data["user_id"],
                vendor_id=data["vendor_id"],
                vendor_user_role=VendorUserRole(data["vendor_user_role"]),
                created_by=created_by,
                updated_by=updated_by,
            )

            VendorUserRepository.create(vendor_user)
            db.session.commit()

            logger.info("Vendor user created successfully: %s", vendor_user.id)
            return vendor_user

        except Exception:
            db.session.rollback()
            logger.exception("Failed to create vendor user in service layer")
            raise
