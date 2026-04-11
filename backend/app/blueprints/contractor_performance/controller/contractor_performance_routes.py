from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.contractor_performance.services.contractor_performance_service import ContractorPerformanceService
from app.blueprints.contractor_performance.schemas import contractor_performance_schema, contractor_performances_schema


contractor_performance_bp = Blueprint('contractor_performance', __name__)



# Get all contractor performances
@contractor_performance_bp.get('/')
def get_all_contractor_performances():
    try:
        contractor_performances = ContractorPerformanceService.get_all_contractor_performances()
        return jsonify(contractor_performances_schema.dump(contractor_performances)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific contractor performance
@contractor_performance_bp.get('/<contractor_performance_id>')
def get_contractor_performance(contractor_performance_id):
    try:
        contractor_performance = ContractorPerformanceService.get_contractor_performance(contractor_performance_id)
        
        if not contractor_performance:
            return jsonify({'error': 'Contractor performance not found'}), 404
        
        return jsonify(contractor_performance_schema.dump(contractor_performance)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new contractor performance
@contractor_performance_bp.post('/')
def create_contractor_performance():
    try:
        data = request.get_json()
        
        validated_data = contractor_performance_schema.load(data)
        
        contractor_performance = ContractorPerformanceService.create_contractor_performance(validated_data)
        
        return jsonify(contractor_performance_schema.dump(contractor_performance)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing contractor performance
@contractor_performance_bp.put('/<contractor_performance_id>')
def update_contractor_performance(contractor_performance_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = contractor_performance_schema.load(data)
        
        contractor_performance = ContractorPerformanceService.update_contractor_performance(contractor_performance_id, validated_data)
        
        if not contractor_performance:
            return jsonify({'error': 'Contractor performance not found'}), 404
        
        
        return jsonify(contractor_performance_schema.dump(contractor_performance)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a contractor performance
@contractor_performance_bp.delete('/<contractor_performance_id>')
def delete_contractor_performance(contractor_performance_id):
    try:
        contractor_performance = ContractorPerformanceService.get_contractor_performance(contractor_performance_id)
        
        if not contractor_performance:
            return jsonify({'error': 'Contractor performance not found'}), 404
        
        ContractorPerformanceService.delete_contractor_performance(contractor_performance_id)
        return jsonify({'message': 'Contractor performance deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500