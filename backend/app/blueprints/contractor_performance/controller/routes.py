from flask import Blueprint, request, jsonify
from app.blueprints.contractor_performance.services.service import ContractorPerformanceService
from app.blueprints.contractor_performance.schemas import contractor_performance_scehma, contractor_performances_schema


contractor_performances_bp = Blueprint('contractor_performances', __name__)



# Get all contractor performances
@contractor_performances_bp.route('/', methods=['GET'])
def get_contractor_performances():
    try:
        contractor_performances = ContractorPerformanceService.get_all_contractor_performances()
        return jsonify(contractor_performances_schema.dump(contractor_performances)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific contractor performance
@contractor_performances_bp.route('/<contractor_performance_id>', methods=['GET'])
def get_contractor_performance(contractor_performance_id):
    try:
        contractor_performance = ContractorPerformanceService.get_contractor_performance(contractor_performance_id)
        if not contractor_performance:
            return jsonify({'error': 'Contractor performance not found'}), 404
        return jsonify(contractor_performances_schema.dump(contractor_performance)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new contractor performance
@contractor_performances_bp.route('/', methods=['POST'])
def create_contractor_performance():
    try:
        data = request.get_json()
        contractor_performance = ContractorPerformanceService.create_contractor_performance(data)
        return jsonify(contractor_performances_schema.dump(contractor_performance)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing contractor performance
@contractor_performances_bp.route('/<contractor_performance_id>', methods=['PUT'])
def update_contractor_performance(contractor_performance_id):
    try:
        data = request.get_json()
        contractor_performance = ContractorPerformanceService.update_contractor_performance(contractor_performance_id, data)
        if not contractor_performance:
            return jsonify({'error': 'Contractor performance not found'}), 404
        return jsonify(contractor_performances_schema.dump(contractor_performance)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a contractor performance
@contractor_performances_bp.route('/<contractor_performance_id>', methods=['DELETE'])
def delete_contractor_performance(contractor_performance_id):
    try:
        contractor_performance = ContractorPerformanceService.get_contractor_performance(contractor_performance_id)
        if not contractor_performance:
            return jsonify({'error': 'Contractor performance not found'}), 404
        ContractorPerformanceService.delete_contractor_performance(contractor_performance_id)
        return jsonify({'message': 'Contractor performance deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500