from ..repositories.address_repository import AddressRepository
import logging

logger = logging.getLogger(__name__)


class AddressService:

        
    @staticmethod
    def create_address(data: dict):
        try:
            return AddressRepository.create(data)
        except Exception:
            logger.exception("Error creating address")
            raise
