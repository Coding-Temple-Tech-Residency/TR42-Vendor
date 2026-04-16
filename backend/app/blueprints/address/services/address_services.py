from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.blueprints.address.model import Address
from app.blueprints.address.repositories.address_repositories import AddressRepository
import logging

logger = logging.getLogger(__name__)


class AddressService:

    @staticmethod
    def create_address(data: dict) -> Address:
        try:
            address = Address(
                street=data["street"],
                city=data["city"],
                state=data["state"],
                zip=data["zip"],
                country=data.get("country", "USA"),
                created_by=data["created_by"],
                updated_by=data.get("updated_by"),
            )

            AddressRepository.create(address)
            db.session.commit()
            return address

        except IntegrityError:
            db.session.rollback()
            logger.exception("Database error creating address")
            raise ValueError("Address creation failed due to a database constraint")

        except Exception:
            db.session.rollback()
            logger.exception("Error creating address")
            raise
