from app.extensions import db
from .model import Address
import logging

logger = logging.getLogger(__name__)


class AddressRepository:


    @staticmethod
    def create(data: dict):
        try:
            address = Address(
                **data,
                created_by="system",
                updated_by="system"
            )
            db.session.add(address)
            db.session.commit()
            return address
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create address")
            raise

    