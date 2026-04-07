from flask import Blueprint, jsonify, request
import logging

from marshmallow import ValidationError
from app.blueprints.registration.services.registration_services import (
    RegistrationService,
)

logger = logging.getLogger(__name__)


registration_bp = Blueprint(
    "registration_bp",
    __name__,
)


@registration_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    logger.debug("Registering a new vendor")

    if not data:
        logger.warning("No input data provided for vendor creation")
        return jsonify({"error": "No input data provided"}), 400

    try:
        result = RegistrationService.register_vendor_account(data)
        return jsonify(result), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except ValueError as err:
        return jsonify({"error": str(err)}), 400
