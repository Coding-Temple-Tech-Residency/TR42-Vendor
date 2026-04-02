from flask import request

from app.blueprints.address.address_service import AddressService
from .schemas import addresses_schema, address_schema
import logging
from flask import Blueprint

logger = logging.getLogger(__name__)

address_bp = Blueprint("address", __name__)

@address_bp.post("/")
def create_address():
    
    try:
        data = request.get_json()
        new_address = AddressService.create_address(data)
        return address_schema.dump(new_address), 201
    except Exception:
        logger.exception("Error creating address")
        return {"error": "Failed to create address"}, 500


