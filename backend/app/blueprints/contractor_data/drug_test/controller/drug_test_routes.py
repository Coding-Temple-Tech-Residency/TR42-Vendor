from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
import logging

from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.vendor_user.model import VendorUserRole
from app.blueprints.contractor_data.drug_test.schemas import (
    drug_test_schema,
    drug_test_create_schema,
    drug_tests_schema,
)
from app.blueprints.contractor_data.drug_test.services.drug_test_services import (
    DrugTestService,
)

logger = logging.getLogger(__name__)

drug_test_bp = Blueprint("drug_test_bp", __name__)


@drug_test_bp.post("/contractors/<string:contractor_id>/drug-tests")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_drug_test(current_user, vendor_link, vendor_id, contractor_id):
    try:
        drug_test_data = request.get_json(silent=True)
        logger.debug("Creating drug test")

        if not drug_test_data:
            logger.debug("No input data provided for drug test creation")
            return {"error": "No input data provided"}, 400

        validated_data = drug_test_create_schema.load(drug_test_data)

        if not isinstance(validated_data, dict):
            logger.warning("Validated drug test data is not a dictionary")
            return {"error": "Invalid drug test data"}, 400

        new_drug_test = DrugTestService.create_drug_test(
            contractor_id=contractor_id,
            validated_data=validated_data,
            created_by=current_user.id,
            updated_by=current_user.id,
        )

        logger.info("Drug test created successfully")
        return jsonify(drug_test_schema.dump(new_drug_test)), 201

    except ValidationError as err:
        logger.warning(f"Validation error while creating drug test: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error creating drug test")
        return {"error": "An error occurred while creating the drug test"}, 500


@drug_test_bp.get("/contractors/<string:contractor_id>/drug-tests")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_drug_tests(current_user, vendor_link, vendor_id, contractor_id):
    try:
        drug_tests = DrugTestService.get_drug_tests_by_contractor(contractor_id)
        return jsonify(drug_tests_schema.dump(drug_tests)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while fetching drug tests: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error fetching drug tests")
        return {"error": "An error occurred while fetching drug tests"}, 500


@drug_test_bp.put("/drug-tests/<string:drug_test_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_drug_test(current_user, vendor_link, vendor_id, drug_test_id):
    try:
        drug_test_data = request.get_json(silent=True)
        logger.debug("Updating drug test")

        if not drug_test_data:
            logger.debug("No input data provided for drug test update")
            return {"error": "No input data provided"}, 400

        validated_data = drug_test_create_schema.load(
            drug_test_data,
            partial=True,
        )

        if not isinstance(validated_data, dict):
            logger.warning("Validated drug test data is not a dictionary")
            return {"error": "Invalid drug test data"}, 400

        updated_drug_test = DrugTestService.update_drug_test(
            drug_test_id=drug_test_id,
            validated_data=validated_data,
            updated_by=current_user.id,
        )

        if not updated_drug_test:
            return {"error": "Drug test not found"}, 404

        logger.info("Drug test updated successfully")
        return jsonify(drug_test_schema.dump(updated_drug_test)), 200

    except ValidationError as err:
        logger.warning(f"Validation error while updating drug test: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
    except Exception:
        logger.exception("Error updating drug test")
        return {"error": "An error occurred while updating the drug test"}, 500


@drug_test_bp.delete("/drug-tests/<string:drug_test_id>")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def delete_drug_test(current_user, vendor_link, vendor_id, drug_test_id):
    try:
        deleted = DrugTestService.delete_drug_test(drug_test_id)

        if not deleted:
            return {"error": "Drug test not found"}, 404

        return jsonify({"message": "Drug test deleted"}), 200

    except Exception:
        logger.exception("Error deleting drug test")
        return {"error": "An error occurred while deleting the drug test"}, 500
