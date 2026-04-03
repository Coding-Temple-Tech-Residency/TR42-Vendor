from ..repositories.address_repository import AddressRepository
import logging

logger = logging.getLogger(__name__)


class AddressService:

    @staticmethod
    def get_all_addresses():
        try:
            return AddressRepository.get_all()
        except Exception:
            logger.exception("Error fetching addresses")
            raise
       

    @staticmethod
    def get_address(address_id: str):
        try:
            return AddressRepository.get_by_id(address_id)
        except Exception:
            logger.exception("Error fetching address")
            raise
        

    @staticmethod
    def create_address(data: dict):
        try:
            return AddressRepository.create(data)
        except Exception:
            logger.exception("Error creating address")
            raise
    @staticmethod
    def update_address(address_id: str, data: dict):
        try:
            address = AddressRepository.get_by_id(address_id)
            if not address:
                return None
            return AddressRepository.update(address, data)
        except Exception:
            logger.exception("Error updating address")
            raise
    @staticmethod
    def delete_address(address_id: str):
        try:
            address = AddressRepository.get_by_id(address_id)
            if not address:
                return None
            AddressRepository.delete(address)
            return True
        except Exception:
            logger.exception("Error deleting address")
            raise