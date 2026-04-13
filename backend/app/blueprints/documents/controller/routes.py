from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.documents.services.service import BackgroundCheckService, DrugTestService, ComplianceDocumentService
from app.blueprints.documents.schemas import background_check_schema, background_checks_schema, drug_test_schema, drug_tests_schema, compliance_document_schema, compliance_documents_schema

background_check_bp = Blueprint('background_check', __name__)



# Get all background checks
@background_check_bp.get('/')
def get_all_background_checks():
    try:
        background_checks = BackgroundCheckService.get_all_background_checks()
        return jsonify(background_checks_schema.dump(background_checks)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific background check
@background_check_bp.get('/<background_check_id>')
def get_background_check(background_check_id):
    try:
        background_check = BackgroundCheckService.get_background_check(background_check_id)
        
        if not background_check:
            return jsonify({'error': 'Background check not found'}), 404
        
        return jsonify(background_check_schema.dump(background_check)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new background check
@background_check_bp.post('/')
def create_background_check():
    try:
        data = request.get_json()
        
        validated_data = background_check_schema.load(data)
        
        background_check = BackgroundCheckService.create_background_check(validated_data)
        
        return jsonify(background_check_schema.dump(background_check)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing background check
@background_check_bp.put('/<background_check_id>')
def update_background_check(background_check_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = background_check_schema.load(data)
        
        background_check = BackgroundCheckService.update_background_check(background_check_id, validated_data)
        
        if not background_check:
            return jsonify({'error': 'Background check not found'}), 404
        
        
        return jsonify(background_check_schema.dump(background_check)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a background check
@background_check_bp.delete('/<background_check_id>')
def delete_background_check(background_check_id):
    try:
        background_check = BackgroundCheckService.get_background_check(background_check_id)
        
        if not background_check:
            return jsonify({'error': 'Background check not found'}), 404
        
        BackgroundCheckService.delete_background_check(background_check_id)
        return jsonify({'message': 'Background check deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    

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
    
    
compliance_document_bp = Blueprint('compliance_document', __name__)

# Get all compliance documents
@compliance_document_bp.get('/')
def get_all_compliance_documents():
    try:
        compliance_documents = ComplianceDocumentService.get_all_compliance_documents()
        return jsonify(compliance_document_schema.dump(compliance_documents)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific compliance document
@compliance_document_bp.get('/<compliance_document_id>')
def get_compliance_document(compliance_document_id):
    try:
        compliance_document = ComplianceDocumentService.get_compliance_document(compliance_document_id)
        
        if not compliance_document:
            return jsonify({'error': 'Compliance document not found'}), 404
        
        return jsonify(compliance_document_schema.dump(compliance_document)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new compliance document
@compliance_document_bp.post('/')
def create_compliance_document():
    try:
        data = request.get_json()
        
        validated_data = compliance_document_schema.load(data)
        
        compliance_document = ComplianceDocumentService.create_compliance_document(validated_data)
        
        return jsonify(compliance_document_schema.dump(compliance_document)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing compliance document
@compliance_document_bp.put('/<compliance_document_id>')
def update_compliance_document(compliance_document_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = compliance_document_schema.load(data)
        
        compliance_document = ComplianceDocumentService.update_compliance_document(compliance_document_id, validated_data)
        
        if not compliance_document:
            return jsonify({'error': 'Compliance document not found'}), 404
        
        
        return jsonify(compliance_document_schema.dump(compliance_document)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a compliance document
@compliance_document_bp.delete('/<compliance_document_id>')
def delete_compliance_document(compliance_document_id):
    try:
        compliance_document = ComplianceDocumentService.get_compliance_document(compliance_document_id)
        
        if not compliance_document:
            return jsonify({'error': 'Compliance document not found'}), 404
        
        ComplianceDocumentService.delete_compliance_document(compliance_document_id)
        return jsonify({'message': 'Compliance document deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


