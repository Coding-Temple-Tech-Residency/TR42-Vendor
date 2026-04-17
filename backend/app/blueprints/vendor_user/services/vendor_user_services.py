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

            vendor_user = VendorUser(
                user_id=data["user_id"],
                vendor_id=data["vendor_id"],
                role=VendorUserRole(data["role"]),
                created_by_user_id=data["created_by_user_id"],
                updated_by_user_id=data["updated_by_user_id"]

            )

            VendorUserRepository.create(vendor_user)
            db.session.commit()

            logger.info("Vendor user created successfully: %s", vendor_user.id)
            return vendor_user

        except Exception:
            db.session.rollback()
            logger.exception("Failed to create vendor user in service layer")
            raise
    
    @staticmethod
    def get_all_by_user(user_id: str):
        try:
            logger.debug("Service: fetching vendor users for user_id=%s", user_id)
            return VendorUserRepository.get_all_by_user(user_id)
        except Exception:
            logger.exception("Service failed to fetch vendor users for user_id=%s", user_id)
            raise



    @staticmethod
    def get_by_user_and_vendor(user_id: str, vendor_id: str):
        try:
            logger.debug(
                "Service: fetching vendor user link for user_id=%s and vendor_id=%s",
                user_id,
                vendor_id,
            )
            return VendorUserRepository.get_by_user_and_vendor(user_id, vendor_id)
        except Exception:
            logger.exception("Service failed to fetch vendor user link")
            raise


    @staticmethod
    def get_by_id(id: str):
        logger.debug("Retrieving vendor user by id=%s", id)
        return VendorUserRepository.get_by_id(id)
    
    @staticmethod
    def delete(id: str):
        vendor_user = VendorUserRepository.get_by_id(id)
        if not vendor_user:
            return None

        VendorUserRepository.delete(vendor_user)
        db.session.commit()
        return True