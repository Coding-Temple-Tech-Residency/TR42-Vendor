from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
import logging

from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.vendor_user.model import VendorUserRole
from app.blueprints.contractor_data.license.schemas import (
    license_schema,
    license_create_schema,
    licenses_schema,
)
from app.blueprints.contractor_data.license.services.license_services import (
    LicenseService,
)

logger = logging.getLogger(__name__)

license_bp = Blueprint("license_bp", __name__)


@license_bp.post("/contractors/<string:contractor_id>/licenses")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_license(current_user, vendor_link, vendor_id, contractor_id):
    try:
        license_data = request.get_json(silent=True)
        logger.debug("Creating license")

        if not license_data:
            logger.debug("No input data provided for license creation")
            return {"error": "No input data provided"}, 400

        validated_data = license_create_schema.load(license_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated license data is not a dictionary")
            return {"error": "Invalid license data"}, 400

        new_license = LicenseService.create_license(
            contractor_id=contractor_id,
            validated_data=validated_data,
            created_by=current_user.id,
            updated_by=current_user.id,
        )

        logger.info("License created successfully")
        return jsonify(license_schema.dump(new_license)), 201

    except ValidationError as err:
        logger.warning(f"Validation error while creating license: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating license")
        return {"error": "An error occurred while creating the license"}, 500


@license_bp.get("/contractors/<string:contractor_id>/licenses")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_licenses(current_user, vendor_link, vendor_id, contractor_id):
    try:
        licenses = LicenseService.get_licenses_by_contractor(contractor_id)
        return jsonify(licenses_schema.dump(licenses)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while fetching licenses: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error fetching licenses")
        return {"error": "An error occurred while fetching licenses"}, 500


@license_bp.put("/licenses/<string:license_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_license(current_user, vendor_link, vendor_id, license_id):
    try:
        license_data = request.get_json(silent=True)
        logger.debug("Updating license")

        if not license_data:
            logger.debug("No input data provided for license update")
            return {"error": "No input data provided"}, 400

        validated_data = license_create_schema.load(
            license_data,
            partial=True,
        )

        if not isinstance(validated_data, dict):
            logger.warning("Validated license data is not a dictionary")
            return {"error": "Invalid license data"}, 400

        updated_license = LicenseService.update_license(
            license_id=license_id,
            validated_data=validated_data,
            updated_by=current_user.id,
        )

        if not updated_license:
            return {"error": "License not found"}, 404

        logger.info("License updated successfully")
        return jsonify(license_schema.dump(updated_license)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while updating license: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error updating license")
        return {"error": "An error occurred while updating the license"}, 500


@license_bp.delete("/licenses/<string:license_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def delete_license(current_user, vendor_link, vendor_id, license_id):
    try:
        deleted = LicenseService.delete_license(license_id)

        if not deleted:
            return {"error": "License not found"}, 404

        return jsonify({"message": "License deleted"}), 200

    except Exception:
        logger.exception("Error deleting license")
        return {"error": "An error occurred while deleting the license"}, 500
