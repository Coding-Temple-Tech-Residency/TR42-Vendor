from app.blueprints.vendor.repositories.vendors_repository import VendorRepository
from app.blueprints.vendor.model import Vendor
import logging


logger = logging.getLogger(__name__)


class VendorService:

    @staticmethod
    def get_all_vendors():
        try:
            logger.debug("Retrieving all vendors from service layer")
            return VendorRepository.get_all()
        except Exception:
            logger.exception("Failed to retrieve vendors in service layer")
            raise

    @staticmethod
    def create_vendor(vendor: Vendor):
        try:
            logger.info(
                "Creating vendor in service layer with company_name: %s",
                vendor.company_name,
            )

            existing_vendor = VendorRepository.get_by_company_name(vendor.company_name)
            if existing_vendor:
                raise ValueError("Vendor with this company name already exists")

            return VendorRepository.create(vendor)

        except Exception:
            logger.exception("Failed to create vendor in service layer")
            raise