from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
import logging

from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.vendor_user.model import VendorUserRole
from app.blueprints.contractor_data.background_check.schemas import (
    background_check_schema,
    background_check_create_schema,
    background_checks_schema,
)
from app.blueprints.contractor_data.background_check.services.background_check_services import (
    BackgroundCheckService,
)

logger = logging.getLogger(__name__)

background_check_bp = Blueprint("background_check_bp", __name__)


@background_check_bp.post("/contractors/<string:contractor_id>/background-checks")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_background_check(current_user, vendor_link, vendor_id, contractor_id):
    try:
        background_check_data = request.get_json(silent=True)
        logger.debug("Creating background check")

        if not background_check_data:
            logger.debug("No input data provided for background check creation")
            return {"error": "No input data provided"}, 400

        validated_data = background_check_create_schema.load(background_check_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated background check data is not a dictionary")
            return {"error": "Invalid background check data"}, 400

        new_background_check = BackgroundCheckService.create_background_check(
            contractor_id=contractor_id,
            validated_data=validated_data,
            created_by=current_user.id,
            updated_by=current_user.id,
        )

        logger.info("Background check created successfully")
        return jsonify(background_check_schema.dump(new_background_check)), 201

    except ValidationError as err:
        logger.warning(
            f"Validation error while creating background check: {err.messages}"
        )
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating background check")
        return {"error": "An error occurred while creating the background check"}, 500


@background_check_bp.get("/contractors/<string:contractor_id>/background-checks")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_background_checks(current_user, vendor_link, vendor_id, contractor_id):
    try:
        background_checks = BackgroundCheckService.get_background_checks_by_contractor(
            contractor_id
        )
        return jsonify(background_checks_schema.dump(background_checks)), 200

    except ValidationError as err:
        logger.warning(
            f"Validation error while fetching background checks: {err.messages}"
        )
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error fetching background checks")
        return {"error": "An error occurred while fetching background checks"}, 500


@background_check_bp.put("/background-checks/<string:background_check_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_background_check(current_user, vendor_link, vendor_id, background_check_id):
    try:
        background_check_data = request.get_json(silent=True)
        logger.debug("Updating background check")

        if not background_check_data:
            logger.debug("No input data provided for background check update")
            return {"error": "No input data provided"}, 400

        validated_data = background_check_create_schema.load(
            background_check_data,
            partial=True,
        )

        if not isinstance(validated_data, dict):
            logger.warning("Validated background check data is not a dictionary")
            return {"error": "Invalid background check data"}, 400

        updated_background_check = BackgroundCheckService.update_background_check(
            background_check_id=background_check_id,
            validated_data=validated_data,
            updated_by=current_user.id,
        )

        if not updated_background_check:
            return {"error": "Background check not found"}, 404

        logger.info("Background check updated successfully")
        return jsonify(background_check_schema.dump(updated_background_check)), 200

    except ValidationError as err:
        logger.warning(
            f"Validation error while updating background check: {err.messages}"
        )
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error updating background check")
        return {"error": "An error occurred while updating the background check"}, 500


@background_check_bp.delete("/background-checks/<string:background_check_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def delete_background_check(current_user, vendor_link, vendor_id, background_check_id):
    try:
        deleted = BackgroundCheckService.delete_background_check(background_check_id)

        if not deleted:
            return {"error": "Background check not found"}, 404

        return jsonify({"message": "Background check deleted"}), 200

    except Exception:
        logger.exception("Error deleting background check")
        return {"error": "An error occurred while deleting the background check"}, 500
