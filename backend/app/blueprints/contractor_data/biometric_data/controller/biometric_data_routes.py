from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
import logging

from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.vendor_user.model import VendorUserRole
from app.blueprints.contractor_data.biometric_data.schemas import (
    biometric_data_schema,
    biometric_data_create_schema,
    biometric_data_list_schema,
)
from app.blueprints.contractor_data.biometric_data.services.biometric_data_services import (
    BiometricDataService,
)

logger = logging.getLogger(__name__)

biometric_data_bp = Blueprint("biometric_data_bp", __name__)


@biometric_data_bp.post("/contractors/<string:contractor_id>/biometric-data")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_biometric_data(current_user, vendor_link, vendor_id, contractor_id):
    try:
        biometric_data_payload = request.get_json(silent=True)
        logger.debug("Creating biometric data")

        if not biometric_data_payload:
            logger.debug("No input data provided for biometric data creation")
            return {"error": "No input data provided"}, 400

        validated_data = biometric_data_create_schema.load(biometric_data_payload)

        if not isinstance(validated_data, dict):
            logger.warning("Validated biometric data is not a dictionary")
            return {"error": "Invalid biometric data"}, 400

        new_biometric_data = BiometricDataService.create_biometric_data(
            contractor_id=contractor_id,
            validated_data=validated_data,
            created_by=current_user.id,
            updated_by=current_user.id,
        )

        logger.info("Biometric data created successfully")
        return jsonify(biometric_data_schema.dump(new_biometric_data)), 201

    except ValidationError as err:
        logger.warning(
            f"Validation error while creating biometric data: {err.messages}"
        )
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating biometric data")
        return {"error": "An error occurred while creating the biometric data"}, 500


@biometric_data_bp.get("/contractors/<string:contractor_id>/biometric-data")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_biometric_data(current_user, vendor_link, vendor_id, contractor_id):
    try:
        biometric_records = BiometricDataService.get_biometric_data_by_contractor(
            contractor_id
        )
        return jsonify(biometric_data_list_schema.dump(biometric_records)), 200

    except ValidationError as err:
        logger.warning(
            f"Validation error while fetching biometric data: {err.messages}"
        )
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error fetching biometric data")
        return {"error": "An error occurred while fetching biometric data"}, 500


@biometric_data_bp.put("/biometric-data/<string:biometric_data_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_biometric_data(current_user, vendor_link, vendor_id, biometric_data_id):
    try:
        biometric_data = request.get_json(silent=True)
        logger.debug("Updating biometric data")

        if not biometric_data:
            logger.debug("No input data provided for biometric data update")
            return {"error": "No input data provided"}, 400

        validated_data = biometric_data_create_schema.load(
            biometric_data,
            partial=True,
        )

        if not isinstance(validated_data, dict):
            logger.warning("Validated biometric data is not a dictionary")
            return {"error": "Invalid biometric data"}, 400

        updated_biometric_data = BiometricDataService.update_biometric_data(
            biometric_data_id=biometric_data_id,
            validated_data=validated_data,
            updated_by=current_user.id,
        )

        if not updated_biometric_data:
            return {"error": "Biometric data not found"}, 404

        logger.info("Biometric data updated successfully")
        return jsonify(biometric_data_schema.dump(updated_biometric_data)), 200

    except ValidationError as err:
        logger.warning(
            f"Validation error while updating biometric data: {err.messages}"
        )
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error updating biometric data")
        return {"error": "An error occurred while updating the biometric data"}, 500


@biometric_data_bp.delete("/biometric-data/<string:biometric_data_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def delete_biometric_data(current_user, vendor_link, vendor_id, biometric_data_id):
    try:
        deleted = BiometricDataService.delete_biometric_data(biometric_data_id)

        if not deleted:
            return {"error": "Biometric data not found"}, 404

        return jsonify({"message": "Biometric data deleted"}), 200

    except Exception:
        logger.exception("Error deleting biometric data")
        return {"error": "An error occurred while deleting the biometric data"}, 500
