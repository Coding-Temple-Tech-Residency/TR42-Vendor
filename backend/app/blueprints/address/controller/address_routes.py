from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.blueprints.address.schemas import address_schema
from app.blueprints.address.services.address_services import AddressService
import logging

logger = logging.getLogger(__name__)

address_bp = Blueprint("address_bp", __name__)


@address_bp.post("/")
def create_address():
    try:
        data = request.get_json(silent=True) or {}

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        validated_data = address_schema.load(data)
        new_address = AddressService.create_address(validated_data)

        return jsonify(address_schema.dump(new_address)), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    except Exception:
        logger.exception("Error creating address")
        return jsonify({"error": "Failed to create address"}), 500
