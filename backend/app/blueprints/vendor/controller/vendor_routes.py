from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.blueprints.vendor.model import Vendor
from app.blueprints.vendor.services.vendor_services import VendorService
from app.blueprints.vendor.schemas import vendor_schema, vendors_schema
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


@vendor_bp.get("/")
def get_all_vendors():
    try:
        logger.debug("Fetching all vendors")
        vendors = VendorService.get_all_vendors()
        logger.info(f"Retrieved {len(vendors)} vendors")
        return jsonify(vendors_schema.dump(vendors)), 200
    except Exception:
        logger.exception("Error fetching vendors")
        return {"error": "An error occurred while fetching vendors"}, 500


@vendor_bp.get("/<vendor_id>")
def get_vendor_by_id(vendor_id: str):
    try:
        logger.debug("Fetching vendor with id")
        vendor = VendorService.get_vendor_by_id(vendor_id)

        if not vendor:
            logger.debug(f"Vendor with id not found")
            return {"error": "Vendor not found"}, 404

        logger.info("Vendor retrieved successfully")
        return jsonify(vendor_schema.dump(vendor)), 200
    except Exception:
        logger.exception("Error fetching vendor with id")
        return {"error": "An error occurred while fetching the vendor"}, 500


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
        return jsonify(vendor_registration_schema.dump(new_vendor)), 201

    except ValidationError as err:
        logger.warning(f"Validation error while creating vendor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating vendor")
        return {"error": "An error occurred while creating the vendor"}, 500


@vendor_bp.put("/<int:vendor_id>")
def update_vendor(vendor_id: int):
    try:
        data = request.get_json()
        logger.debug("Updating vendor with id")

        if not data:
            logger.warning("No input data provided for vendor update")
            return {"error": "No input data provided"}, 400

        existing_vendor = VendorService.get_vendor_by_id(vendor_id)
        if not existing_vendor:
            logger.warning("Vendor with id not found for update")
            return {"error": "Vendor not found"}, 404

        validated_data: Vendor = vendor_schema.load(data, partial=True)
        logger.debug(f"Vendor data validated successfully for vendor id {vendor_id}")

        updated_vendor: Vendor = VendorService.update_vendor(vendor_id, validated_data)

        logger.info("Vendor updated successfully")
        return vendor_schema.jsonify(updated_vendor), 200

    except ValidationError as err:
        logger.warning(f"Validation error while updating vendor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception(f"Error updating vendor with id")
        return {"error": "An error occurred while updating the vendor"}, 500


@vendor_bp.delete("/<int:vendor_id>")
def delete_vendor(vendor_id: int):
    try:
        logger.debug("Deleting vendor with id")

        existing_vendor = VendorService.get_vendor_by_id(vendor_id)
        if not existing_vendor:
            logger.warning("Vendor with id not found for deletion")
            return {"error": "Vendor not found"}, 404

        VendorService.delete_vendor(vendor_id)

        logger.info("Vendor deleted successfully")
        return {"message": "Vendor deleted successfully"}, 200

    except Exception:
        logger.exception("Error deleting vendor with id")
        return {"error": "An error occurred while deleting the vendor"}, 500
