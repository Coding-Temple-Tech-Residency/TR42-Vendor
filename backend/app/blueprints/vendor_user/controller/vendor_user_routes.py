from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.blueprints.vendor_user.services.vendor_user_services import VendorUserService
from app.blueprints.vendor_user.schemas import vendor_user_schema, vendor_users_schema
import logging
from app.blueprints.vendor_user.model import VendorUser

logger = logging.getLogger(__name__)

vendor_user_bp = Blueprint("vendor_user", __name__)




@vendor_user_bp.get("/")
def get_all_vendor_users():
    try:
        logger.debug("Fetching all vendor users")
        users = VendorUserService.get_all_vendor_users()

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
        new_vendor_user = VendorUserService.add_vendor_user_to_vendor(data)

        logger.info(f"Created vendor user in repo: {new_vendor_user.id}")
        return jsonify(vendor_user_schema.dump(new_vendor_user)), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    except Exception as e:
        logger.exception(f"Error creating vendor user: {str(e)}")
        return jsonify({"error": "An error occurred while creating the user"}), 500
    

# GET BY ID
@vendor_user_bp.get("/<id>")
def get_vendor_user(id):
    try:
        vendor_user = VendorUserService.get_vendor_user_by_id(id)
        if not vendor_user:
            return {"error": "VendorUser not found"}, 404
        return jsonify(vendor_user_schema.dump(vendor_user)), 200
    except Exception as e:
        logger.error(str(e))
        return {"error": "An error occurred while fetching the user"}, 500


# GET USERS FOR A VENDOR
@vendor_user_bp.get("/vendor/<vendor_id>")
def get_users_for_vendor(vendor_id):
    try:
        vendor_users = VendorUserService.get_users_by_vendor(vendor_id)
        return jsonify(vendor_users_schema.dump(vendor_users)), 200
    except Exception as e:
        logger.error(str(e))
        return {"error": "An error occurred while fetching users for the vendor"}, 500


# GET VENDORS FOR A USER
@vendor_user_bp.get("/user/<user_id>")
def get_vendors_for_user(user_id):
    try:
        vendor_users = VendorUserService.get_vendors_by_user(user_id)
        return jsonify(vendor_users_schema.dump(vendor_users)), 200
    except Exception as e:
        logger.error(str(e))
        return {"error": "An error occurred while fetching vendors for the user"}, 500


# UPDATE
@vendor_user_bp.put("/<id>")
def update_vendor_user(id):
    try:
        data = request.get_json()
        vendor_user = VendorUserService.update_vendor_user(id, data)
        if not vendor_user:
            return {"error": "VendorUser not found"}, 404
        return jsonify(vendor_user_schema.dump(vendor_user)), 200
    except Exception as e:
        logger.error(str(e))
        return {"error": "An error occurred while updating the user"}, 500


# DELETE
@vendor_user_bp.delete("/<id>")
def delete_vendor_user(id):
    try:
        deleted = VendorUserService.delete_vendor_user(id)
        if not deleted:
            return {"error": "VendorUser not found"}, 404
        return {"message": "VendorUser deleted"}, 200
    except Exception as e:
        logger.error(str(e))
        return {"error": "An error occurred while deleting the user"}, 500