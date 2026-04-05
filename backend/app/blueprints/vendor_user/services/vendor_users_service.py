from app.blueprints.vendor_user.repositories.vendor_users_repository import VendorUserRepository
import uuid
from datetime import datetime
from app.blueprints.vendor_user.model import VendorUser
import logging

logger = logging.getLogger(__name__)

class VendorUserService:

    """
    Retrieve all vendor users from the database.

    Returns:
        list: A list of all VendorUser objects stored in the repository.
              Returns an empty list if no users exist.
    """

    @staticmethod
    def get_all_users():
        try:
            logger.debug("Retrieving all vendor users from service layer")
            return VendorUserRepository.get_all()
        except Exception:
            logger.exception("Failed to retrieve vendor users in service layer")
            raise

    """
        Create a new vendor user record in the database.
        
        Args:
            data (dict): A dictionary containing the vendor user information with the following keys:
                - user_id (str): The ID of the user.
                - vendor_id (str): The ID of the vendor.
                - role (str): The role assigned to the vendor user.
                - created_by (str): The ID of the user who created this record.
                - updated_by (str): The ID of the user who last updated this record.
        
        Returns:
            VendorUser: The created VendorUser object with auto-generated UUID and timestamps.
        
        Raises:
            DatabaseError: If the database operation fails during creation.
        """
    

    @staticmethod
    def create_user(data):
        # Build ORM object with provided data and auto-generated fields
        try:
            logger.debug("Creating vendor user in service layer with data: %s", data)
            new_user = VendorUser(
                id=str(uuid.uuid4()),
                user_id=data.get("user_id"),
                vendor_id=data.get("vendor_id"),
                role=data.get("role"),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
                created_by=data.get("created_by"),
                updated_by=data.get("updated_by"),
            )

            logger.info(f"Vendor user object created in service layer: {new_user.id}")
            return VendorUserRepository.create(new_user)
        except Exception:
            logger.exception("Failed to create vendor user in service layer")
            raise