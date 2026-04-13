from flask import Blueprint, request, jsonify
from ..services.service import ContractorService
from ..schemas import ContractorSchema
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

contractor_bp = Blueprint('contractors', __name__)
schema = ContractorSchema()
schema_many = ContractorSchema(many=True)

# GET all contractors
@contractor_bp.route('/', methods=['GET'])
def get_contractors():
    try:
        contractors = ContractorService.get_all_contractors()
        return jsonify(schema_many.dump(contractors)), 200
    except Exception as e:
        logger.exception("Failed to fetch contractors")
        return jsonify({"error": str(e)}), 500

# GET single contractor
@contractor_bp.route('/<contractor_id>', methods=['GET'])
def get_contractor(contractor_id):
    try:
        contractor = ContractorService.get_contractor(contractor_id)
        if not contractor:
            return jsonify({"error": "Contractor not found"}), 404
        return schema.jsonify(contractor), 200
    except Exception as e:
        logger.exception(f"Failed to fetch contractor {contractor_id}")
        return jsonify({"error": str(e)}), 500

# POST create contractor
@contractor_bp.route('/', methods=['POST'])
def create_contractor():
    try:
        data = request.get_json()
        contractor = ContractorService.create_contractor(data)
        return schema.jsonify(contractor), 201
    except Exception as e:
        logger.exception("Failed to create contractor")
        return jsonify({"error": str(e)}), 500

# PUT update contractor
@contractor_bp.route('/<contractor_id>', methods=['PUT'])
def update_contractor(contractor_id):
    try:
        data = request.get_json()
        contractor = ContractorService.get_contractor(contractor_id)
        if not contractor:
            return jsonify({"error": "Contractor not found"}), 404
        updated = ContractorService.update_contractor(contractor, data)
        return schema.jsonify(updated), 200
    except Exception as e:
        logger.exception(f"Failed to update contractor {contractor_id}")
        return jsonify({"error": str(e)}), 500

# DELETE contractor
@contractor_bp.route('/<contractor_id>', methods=['DELETE'])
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