from server.app.extensions import db
from ..model import VendorUser
import logging


logger = logging.getLogger(__name__)

class VendorUserRepository:

    """
        Retrieve all vendor users from the database.
        
        Returns:
            list: A list of all VendorUser objects in the database.
                  Returns an empty list if no vendor users exist.
        """

    @staticmethod
    def get_all():
        try:
            logger.debug("Fetching all vendor users from database")
            return VendorUser.query.all()
        except Exception:
            logger.exception("Failed to fetch vendor users")
            raise 


    """
        Adds a new VendorUser instance to the database and commits the transaction.

        Args:
            vendor_user (VendorUser): The VendorUser object to be added to the database.

        Returns:
            VendorUser: The VendorUser object that was added to the database.
        """
    @staticmethod
    def create(vendor_user: VendorUser):
        try:
            logger.debug(f"Creating vendor user with ID: {vendor_user.id}")
            db.session.add(vendor_user)
            db.session.commit()
            logger.info(f"Vendor user created successfully: {vendor_user.id}")
            return vendor_user
        except Exception:
            logger.exception(f"Failed to create vendor user: {vendor_user.id}")
            db.session.rollback()
            raise 