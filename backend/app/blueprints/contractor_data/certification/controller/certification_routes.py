from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
import logging

from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.vendor_user.model import VendorUserRole
from app.blueprints.contractor_data.certification.schemas import (
    certification_schema,
    certification_create_schema,
    certifications_schema,
)
from app.blueprints.contractor_data.certification.services.certification_services import (
    CertificationService,
)

logger = logging.getLogger(__name__)

certification_bp = Blueprint("certification_bp", __name__)


@certification_bp.post("/contractors/<string:contractor_id>/certifications")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_certification(current_user, vendor_link, vendor_id, contractor_id):
    try:
        certification_data = request.get_json(silent=True)
        logger.debug("Creating certification")

        if not certification_data:
            logger.debug("No input data provided for certification creation")
            return {"error": "No input data provided"}, 400

        validated_data = certification_create_schema.load(certification_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated certification data is not a dictionary")
            return {"error": "Invalid certification data"}, 400

        new_certification = CertificationService.create_certification(
            contractor_id=contractor_id,
            validated_data=validated_data,
            created_by=current_user.id,
            updated_by=current_user.id,
        )

        logger.info("Certification created successfully")
        return jsonify(certification_schema.dump(new_certification)), 201

    except ValidationError as err:
        logger.warning(f"Validation error while creating certification: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating certification")
        return {"error": "An error occurred while creating the certification"}, 500


@certification_bp.get("/contractors/<string:contractor_id>/certifications")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_certifications(current_user, vendor_link, vendor_id, contractor_id):
    try:
        certifications = CertificationService.get_certifications_by_contractor(
            contractor_id
        )
        return jsonify(certifications_schema.dump(certifications)), 200

    except ValidationError as err:
        logger.warning(
            f"Validation error while fetching certifications: {err.messages}"
        )
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error fetching certifications")
        return {"error": "An error occurred while fetching certifications"}, 500


@certification_bp.put("/certifications/<string:certification_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_certification(current_user, vendor_link, vendor_id, certification_id):
    try:
        certification_data = request.get_json(silent=True)
        logger.debug("Updating certification")

        if not certification_data:
            logger.debug("No input data provided for certification update")
            return {"error": "No input data provided"}, 400

        validated_data = certification_create_schema.load(
            certification_data,
            partial=True,
        )

        if not isinstance(validated_data, dict):
            logger.warning("Validated certification data is not a dictionary")
            return {"error": "Invalid certification data"}, 400

        updated_certification = CertificationService.update_certification(
            certification_id=certification_id,
            validated_data=validated_data,
            updated_by=current_user.id,
        )

        if not updated_certification:
            return {"error": "Certification not found"}, 404

        logger.info("Certification updated successfully")
        return jsonify(certification_schema.dump(updated_certification)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while updating certification: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error updating certification")
        return {"error": "An error occurred while updating the certification"}, 500


@certification_bp.delete("/certifications/<string:certification_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def delete_certification(current_user, vendor_link, vendor_id, certification_id):
    try:
        deleted = CertificationService.delete_certification(certification_id)

        if not deleted:
            return {"error": "Certification not found"}, 404

        return jsonify({"message": "Certification deleted"}), 200

    except Exception:
        logger.exception("Error deleting certification")
        return {"error": "An error occurred while deleting the certification"}, 500
