from app.extensions import db
from app.blueprints.vendor_user.model import VendorUser, VendorUserRole
from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
    VendorUserRepository,
)
from datetime import datetime

import logging

logger = logging.getLogger(__name__)


class VendorUserService:

    @staticmethod
    def get_all_vendor_users():
        try:
            logger.debug("Retrieving all vendor users from service layer")
            return VendorUserRepository.get_all()
        except Exception:
            logger.exception("Failed to retrieve vendor users in service layer")
            raise

    @staticmethod
    def add_vendor_user_to_vendor(data):
        try:
            logger.debug("Creating vendor user in service layer with data: %s", data)

            vendor_user = VendorUser(
                user_id=data["user_id"],
                vendor_id=data["vendor_id"],
                vendor_user_role=VendorUserRole(data["vendor_user_role"]),
                created_by_user_id=data["created_by_user_id"],
                updated_by_user_id=data.get("updated_by_user_id"),
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
    def get_vendor_user_by_id(vendor_user_id):
        try:
            return VendorUserRepository.get_by_id(vendor_user_id)
        except Exception:
            logger.exception("Failed to fetch vendor user by ID")
            raise

    @staticmethod
    def get_users_by_vendor(vendor_id):
        try:
            return VendorUserRepository.get_by_vendor_id(vendor_id)
        except Exception:
            logger.exception("Failed to fetch vendor users by vendor ID")
            raise

    @staticmethod
    def get_vendors_by_user(user_id):
        try:
            return VendorUserRepository.get_by_user_id(user_id)
        except Exception:
            logger.exception("Failed to fetch vendor links by user ID")
            raise

    @staticmethod
    def update_vendor_user(vendor_user_id, data):
        try:
            vendor_user = VendorUserRepository.get_by_id(vendor_user_id)
            if not vendor_user:
                return None

            if "vendor_user_role" in data:
                vendor_user.vendor_user_role = VendorUserRole(data["vendor_user_role"])

            vendor_user.vendor_id = data.get("vendor_id", vendor_user.vendor_id)
            vendor_user.updated_by_user_id = data.get("updated_by_user_id", vendor_user.updated_by_user_id)
            vendor_user.updated_at = datetime.utcnow()

            VendorUserRepository.update(vendor_user)
            db.session.commit()
            return vendor_user

        except Exception:
            db.session.rollback()
            logger.exception("Failed to update vendor user")
            raise

    @staticmethod
    def delete_vendor_user(vendor_user_id):
        try:
            vendor_user = VendorUserRepository.get_by_id(vendor_user_id)
            if not vendor_user:
                return False

            VendorUserRepository.delete(vendor_user)
            db.session.commit()
            return True

        except Exception:
            db.session.rollback()
            logger.exception("Failed to delete vendor user")
            raise