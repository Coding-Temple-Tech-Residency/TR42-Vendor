from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.insurance.services.service import InsuranceService
from app.blueprints.insurance.schemas import insurance_schema, insurances_schema


insurance_bp = Blueprint('insurance', __name__)



# Get all insurances
@insurance_bp.get('/')
def get_all_insurances():
    try:
        insurances = InsuranceService.get_all_insurances()
        return jsonify(insurances_schema.dump(insurances)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific insurance
@insurance_bp.get('/<insurance_id>')
def get_insurance(insurance_id):
    try:
        insurance = InsuranceService.get_insurance(insurance_id)
        
        if not insurance:
            return jsonify({'error': 'Insurance not found'}), 404
        
        return jsonify(insurance_schema.dump(insurance)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new insurance
@insurance_bp.post('/')
def create_insurance():
    try:
        data = request.get_json()
        
        validated_data = insurance_schema.load(data)
        
        insurance = InsuranceService.create_insurance(validated_data)
        
        return jsonify(insurance_schema.dump(insurance)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing insurance
@insurance_bp.put('/<insurance_id>')
def update_insurance(insurance_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = insurance_schema.load(data)
        
        insurance = InsuranceService.update_insurance(insurance_id, validated_data)
        
        if not insurance:
            return jsonify({'error': 'Insurance not found'}), 404
        
        
        return jsonify(insurance_schema.dump(insurance)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a certification
@insurance_bp.delete('/<insurance_id>')
def delete_insurance(insurance_id):
    try:
        insurance = InsuranceService.get_insurance(insurance_id)
        
        if not insurance:
            return jsonify({'error': 'Insurance not found'}), 404
        
        InsuranceService.delete_insurance(insurance_id)
        return jsonify({'message': 'Insurance deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500