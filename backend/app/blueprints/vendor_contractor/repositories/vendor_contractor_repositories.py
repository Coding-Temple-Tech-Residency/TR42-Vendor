from sqlalchemy import select
from app.extensions import db
from app.blueprints.vendor_contractor.model import (
    VendorContractor,
    VendorContractorRole,
)
import logging


logger = logging.getLogger(__name__)


class VendorContractorRepository:

    @staticmethod
    def create(vendor_contractor: VendorContractor):
        try:
            logger.debug("Creating vendor contractor with id")
            db.session.add(vendor_contractor)
            return vendor_contractor
        except Exception:
            logger.exception("Failed to create vendor user")
            raise
