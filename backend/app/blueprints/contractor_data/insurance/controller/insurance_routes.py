from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
import logging

from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.vendor_user.model import VendorUserRole
from app.blueprints.contractor_data.insurance.schemas import (
    insurance_schema,
    insurance_create_schema,
    insurances_schema,
)
from app.blueprints.contractor_data.insurance.services.insurance_services import (
    InsuranceService,
)

logger = logging.getLogger(__name__)

insurance_bp = Blueprint("insurance_bp", __name__)


@insurance_bp.post("/contractors/<string:contractor_id>/insurances")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_insurance(current_user, vendor_link, vendor_id, contractor_id):
    try:
        insurance_data = request.get_json(silent=True)
        logger.debug("Creating insurance")

        if not insurance_data:
            logger.debug("No input data provided for insurance creation")
            return {"error": "No input data provided"}, 400

        validated_data = insurance_create_schema.load(insurance_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated insurance data is not a dictionary")
            return {"error": "Invalid insurance data"}, 400

        new_insurance = InsuranceService.create_insurance(
            contractor_id=contractor_id,
            validated_data=validated_data,
            created_by=current_user.id,
            updated_by=current_user.id,
        )

        logger.info("Insurance created successfully")
        return jsonify(insurance_schema.dump(new_insurance)), 201

    except ValidationError as err:
        logger.warning(f"Validation error while creating insurance: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating insurance")
        return {"error": "An error occurred while creating the insurance"}, 500


@insurance_bp.get("/contractors/<string:contractor_id>/insurances")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_insurances(current_user, vendor_link, vendor_id, contractor_id):
    try:
        insurances = InsuranceService.get_insurances_by_contractor(contractor_id)
        return jsonify(insurances_schema.dump(insurances)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while fetching insurances: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error fetching insurances")
        return {"error": "An error occurred while fetching insurances"}, 500


@insurance_bp.put("/insurances/<string:insurance_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_insurance(current_user, vendor_link, vendor_id, insurance_id):
    try:
        insurance_data = request.get_json(silent=True)
        logger.debug("Updating insurance")

        if not insurance_data:
            logger.debug("No input data provided for insurance update")
            return {"error": "No input data provided"}, 400

        validated_data = insurance_create_schema.load(
            insurance_data,
            partial=True,
        )

        if not isinstance(validated_data, dict):
            logger.warning("Validated insurance data is not a dictionary")
            return {"error": "Invalid insurance data"}, 400

        updated_insurance = InsuranceService.update_insurance(
            insurance_id=insurance_id,
            validated_data=validated_data,
            updated_by=current_user.id,
        )

        if not updated_insurance:
            return {"error": "Insurance not found"}, 404

        logger.info("Insurance updated successfully")
        return jsonify(insurance_schema.dump(updated_insurance)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while updating insurance: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error updating insurance")
        return {"error": "An error occurred while updating the insurance"}, 500


@insurance_bp.delete("/insurances/<string:insurance_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def delete_insurance(current_user, vendor_link, vendor_id, insurance_id):
    try:
        deleted = InsuranceService.delete_insurance(insurance_id)

        if not deleted:
            return {"error": "Insurance not found"}, 404

        return jsonify({"message": "Insurance deleted"}), 200

    except Exception:
        logger.exception("Error deleting insurance")
        return {"error": "An error occurred while deleting the insurance"}, 500
