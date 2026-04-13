from sqlalchemy import select

from app.extensions import db
from app.blueprints.address.model import Address
import logging

logger = logging.getLogger(__name__)


class AddressRepository:

    @staticmethod
    def create(address: Address) -> Address:
        try:
            logger.debug("Adding address to session")
            db.session.add(address)
            return address
        except Exception:
            logger.exception("Failed to add address to session")
            raise

    @staticmethod
    def get_address_by_street(street: str):
        try:
            logger.debug("Fetching address by street")
            return db.session.scalar(select(Address).where(Address.street == street))
        except Exception:
            logger.exception("Failed to fetch address by street")
            raise
