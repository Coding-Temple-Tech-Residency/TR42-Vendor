from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.vendor.schemas import CombinedVendorRegistrationSchema
from app.blueprints.vendor.registration_service import VendorRegistrationService
import logging

logger = logging.getLogger(__name__)

vendor_registration_bp = Blueprint("vendor_registration_bp", __name__, url_prefix="/vendors")


@vendor_registration_bp.post("/register")
def register_vendor():
    try:
        data = request.get_json()
        logger.debug("Received vendor registration payload")

        validated = CombinedVendorRegistrationSchema().load(data)
        logger.debug("Vendor registration data validated successfully")

        result = VendorRegistrationService.register(validated)

        logger.info("Vendor registration completed successfully")
        return jsonify(result), 201

    except ValidationError as err:
        logger.warning(f"Validation error: {err.messages}")
        return {"error": "Validation failed", "messages": err.messages}, 400

    except Exception as e:
        logger.exception(f"Unexpected error during vendor registration: {e}")
        return {"error": str(e)}, 500
