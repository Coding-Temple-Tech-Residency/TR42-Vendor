
from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.blueprints.vendor_user.services.vendor_user_services import VendorUserService
from app.blueprints.vendor_user.schemas import vendor_user_schema, vendor_users_schema
import logging

logger = logging.getLogger(__name__)

vendor_user_bp = Blueprint("vendor_user", __name__)


@vendor_user_bp.get("/")
def get_all_vendor_users():
    try:
        logger.debug("Fetching all vendor users")
        users = VendorUserService.get_all_users()

        logger.info(f"Retrieved {len(users)} users")
        return jsonify(vendor_users_schema.dump(users)), 200

    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        return {"error": "An error occurred while fetching users"}, 500


@vendor_user_bp.post("/")
def create_vendor_user():
    try:
        logger.debug("Creating a new vendor user")
        data = request.get_json()

        logger.info(f"Received vendor user data: {data}")
        new_vendor_user = VendorUserService.add_user_to_vendor(data)

        logger.info(f"Created vendor user in repo: {new_vendor_user.id}")
        return jsonify(vendor_user_schema.dump(new_vendor_user)), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    except Exception as e:
        logger.exception(f"Error creating vendor user: {str(e)}")
        return jsonify({"error": "An error occurred while creating the user"}), 500











































