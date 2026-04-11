from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.drug_test.services.service import DrugTestService
from app.blueprints.drug_test.schemas import drug_test_schema, drug_tests_schema


drug_test_bp = Blueprint('drug_test', __name__)



# Get all drug tests
@drug_test_bp.get('/')
def get_all_drug_tests():
    try:
        drug_tests = DrugTestService.get_all_drug_tests()
        return jsonify(drug_tests_schema.dump(drug_tests)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific drug test
@drug_test_bp.get('/<drug_test_id>')
def get_drug_test(drug_test_id):
    try:
        drug_test = DrugTestService.get_drug_test(drug_test_id)
        
        if not drug_test:
            return jsonify({'error': 'Drug test not found'}), 404
        
        return jsonify(drug_test_schema.dump(drug_test)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new drug test
@drug_test_bp.post('/')
def create_drug_test():
    try:
        data = request.get_json()
        
        validated_data = drug_test_schema.load(data)
        
        drug_test = DrugTestService.create_drug_test(validated_data)
        
        return jsonify(drug_test_schema.dump(drug_test)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing drug test
@drug_test_bp.put('/<drug_test_id>')
def update_drug_test(drug_test_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = drug_test_schema.load(data)
        
        drug_test = DrugTestService.update_drug_test(drug_test_id, validated_data)
        
        if not drug_test:
            return jsonify({'error': 'Drug test not found'}), 404
        
        
        return jsonify(drug_test_schema.dump(drug_test)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a drug test
@drug_test_bp.delete('/<drug_test_id>')
def delete_drug_test(drug_test_id):
    try:
        drug_test = DrugTestService.get_drug_test(drug_test_id)
        
        if not drug_test:
            return jsonify({'error': 'Drug test not found'}), 404
        
        DrugTestService.delete_drug_test(drug_test_id)
        return jsonify({'message': 'Drug test deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500