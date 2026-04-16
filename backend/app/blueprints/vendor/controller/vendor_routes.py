from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.blueprints.vendor.services.vendor_services import VendorService
from app.blueprints.vendor.schemas import vendor_schema
from app.blueprints.registration.schemas import vendor_registration_schema
import logging
from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.vendor_user.model import VendorUserRole

logger = logging.getLogger(__name__)

vendor_bp = Blueprint(
    "vendor_bp",
    __name__,
)


# @vendor_bp.get("/")
# @token_required
# def get_all_vendors():
#     try:
#         logger.debug("Fetching all vendors")
#         vendors = VendorService.get_all_vendors()
#         logger.info(f"Retrieved {len(vendors)} vendors")
#         return jsonify(vendors_schema.dump(vendors)), 200
#     except Exception:
#         logger.exception("Error fetching vendors")
#         return {"error": "An error occurred while fetching vendors"}, 500


@vendor_bp.get("/")
# @token_required
def get_all_vendors():
    try:
        logger.debug("Fetching all vendors")

        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)

        result = VendorService.get_all_paginated(page=page, per_page=per_page)
        return jsonify(result), 200
    except Exception:
        logger.exception("Error fetching vendors")
        return {"error": "An error occurred while fetching vendors"}, 500


@vendor_bp.get("/active")
@token_required
@vendor_membership_required
def get_active_vendor(current_user, vendor_link, vendor_id):
    try:
        vendor = VendorService.get_vendor_by_id(vendor_id)

        if not vendor:
            return jsonify({"error": "Vendor not found"}), 404

        return jsonify(vendor_schema.dump(vendor)), 200
    except Exception:
        logger.exception("Error fetching active vendor")
        return jsonify({"error": "An error occurred while fetching the vendor"}), 500


@vendor_bp.post("/")
@token_required
def create_vendor(current_user):
    try:
        vendor_data = request.get_json(silent=True)
        logger.debug("Creating a new vendor")

        if not vendor_data:
            logger.debug("No input data provided for vendor creation")
            return {"error": "No input data provided"}, 400

        validated_data = vendor_registration_schema.load(vendor_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated data is not a dictionary")
            return {"error": "Invalid vendor data"}, 400

        new_vendor = VendorService.create_vendor(
            validated_data,
            current_user.user_id,
        )

        logger.info("Vendor created successfully")
        return jsonify(vendor_schema.dump(new_vendor)), 200
    except ValidationError as err:
        logger.warning(f"Validation error while creating vendor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating vendor")
        return {"error": "An error occurred while creating the vendor"}, 500


@vendor_bp.put("/<vendor_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN])
def update_vendor(current_user, vendor_link, vendor_id: str):
    try:
        vendor_data = request.get_json(silent=True)
        logger.debug("Updating vendor with id")

        if not vendor_data:
            logger.warning("No input data provided for vendor update")
            return {"error": "No input data provided"}, 400

        updated_vendor = VendorService.update_vendor(vendor_id, vendor_data)

        if not updated_vendor:
            logger.warning(f"Vendor with id not found")
            return {"error": "Vendor not found"}, 404

        logger.info("Vendor updated successfully")
        return jsonify(vendor_schema.dump(updated_vendor)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while updating vendor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception(f"Error updating vendor with id")
        return {"error": "An error occurred while updating the vendor"}, 500


@vendor_bp.delete("/<vendor_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN])
def delete_vendor(current_user, vendor_link, vendor_id: str):
    try:
        logger.debug("Deleting vendor with id")

        deleted = VendorService.delete_vendor(vendor_id)
        if not deleted:
            return {"error": "Vendor not found"}, 404

        logger.info("Vendor deleted successfully")
        return {"message": "Vendor deleted successfully"}, 200

    except Exception:
        logger.exception("Error deleting vendor with id")
        return {"error": "An error occurred while deleting the vendor"}, 500
