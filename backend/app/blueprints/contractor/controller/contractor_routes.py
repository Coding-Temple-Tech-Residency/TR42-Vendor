from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.contractor.services.contractor_services import ContractorService
from app.blueprints.contractor.schemas import (
    contractor_schema,
    contractor_create_schema,
    contractors_schema,
)
from app.blueprints.vendor_user.model import VendorUserRole
import logging
from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)

logger = logging.getLogger(__name__)

contractor_bp = Blueprint("contractor_bp", __name__)


@contractor_bp.post("/")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_contractor(current_user, vendor_link, vendor_id):
    try:
        contractor_data = request.get_json(silent=True)
        logger.debug("Creating a new contractor")

        if not contractor_data:
            logger.debug("No input data provided for contractor creation")
            return {"error": "No input data provided"}, 400

        validated_data = contractor_create_schema.load(contractor_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated data is not a dictionary")
            return {"error": "Invalid contractor data"}, 400

        new_contractor = ContractorService.create_contractor_by_manager(
            validated_data=validated_data,
            vendor_id=vendor_link.vendor_id,
            vendor_manager_id=current_user.id,
        )

        logger.info("Contractor created successfully")
        return jsonify(contractor_schema.dump(new_contractor)), 201
    except ValidationError as err:
        logger.warning(f"Validation error while creating contractor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating contractor")
        return {"error": "An error occurred while creating the contractor"}, 500


@contractor_bp.post("/onboarding/<invite_token>")
def onboard_contractor(invite_token):
    try:
        contractor_data = request.get_json(silent=True)
        logger.debug("Creating a new contractor")

        if not contractor_data:
            logger.debug("No input data provided for contractor creation")
            return {"error": "No input data provided"}, 400

        validated_data = contractor_create_schema.load(contractor_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated data is not a dictionary")
            return {"error": "Invalid contractor data"}, 400

        new_contractor = ContractorService.self_register_contractor(
            validated_data=validated_data, invite_token=invite_token
        )

        logger.info("Contractor created successfully")
        return jsonify(contractor_schema.dump(new_contractor)), 201
    except ValidationError as err:
        logger.warning(f"Validation error while creating contractor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating contractor")
        return {"error": "An error occurred while creating the contractor"}, 500


@contractor_bp.get("/")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_all_vendor_contractors(current_user, vendor_link, vendor_id):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    result = ContractorService.get_all_vendor_contractors_paginated(
        vendor_id=vendor_id,
        page=page,
        per_page=per_page,
    )
    return jsonify(result), 200


@contractor_bp.route("/<string:contractor_id>", methods=["GET"])
def get_contractor(contractor_id):
    contractor = ContractorService.get_contractor(contractor_id)

    if not contractor:
        return jsonify({"error": "Contractor not found"}), 404

    return jsonify(contractor_schema.dump(contractor)), 200


@contractor_bp.put("/<contractor_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_contractor(current_user, vendor_link, contractor_id: str):
    try:
        contractor_data = request.get_json(silent=True)
        logger.debug("Updating contractor")

        if not contractor_data:
            logger.debug("No input data provided for contractor creation")
            return {"error": "No input data provided"}, 400

        updated_contractor = ContractorService.update_contractor(
            contractor_id, contractor_data
        )

        if not updated_contractor:
            logger.warning("Contractor not found")
            return {"error": "Contractor not found"}, 404

        logger.info("Contractor updated successfully")
        return jsonify(contractor_schema.dump(updated_contractor)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while creating contractor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating contractor")
        return {"error": "An error occurred while creating the contractor"}, 500


@contractor_bp.delete("/<contractor_id>")
def delete_contractor(contractor_id):
    try:
        contractor = ContractorService.get_contractor(contractor_id)
        if not contractor:
            return jsonify({"error": "Contractor not found"}), 404
        ContractorService.delete_contractor(contractor)
        return jsonify({"message": "Contractor deleted"}), 200
    except Exception as e:
        logger.exception(f"Failed to delete contractor {contractor_id}")
        return jsonify({"error": str(e)}), 500
