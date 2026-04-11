from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.certifications.services.service import CertificationService
from app.blueprints.certifications.schema import certification_schema, certifications_schema


certification_bp = Blueprint('certifications', __name__)



# Get all certifications
@certification_bp.get('/')
def get_all_certifications():
    try:
        certifications = CertificationService.get_all_certifications()
        return jsonify(certifications_schema.dump(certifications)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific certification
@certification_bp.get('/<certification_id>')
def get_certification(certification_id):
    try:
        certification = CertificationService.get_certification(certification_id)
        
        if not certification:
            return jsonify({'error': 'Certification not found'}), 404
        
        return jsonify(certification_schema.dump(certification)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new certification
@certification_bp.post('/')
def create_certification():
    try:
        data = request.get_json()
        
        validated_data = certification_schema.load(data)
        
        certification = CertificationService.create_certification(validated_data)
        
        return jsonify(certification_schema.dump(certification)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing certification
@certification_bp.put('/<certification_id>')
def update_certification(certification_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = certification_schema.load(data)
        
        certification = CertificationService.update_certification(certification_id, validated_data)
        
        if not certification:
            return jsonify({'error': 'Certification not found'}), 404
        
        
        return jsonify(certification_schema.dump(certification)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a certification
@certification_bp.delete('/<certification_id>')
def delete_certification(certification_id):
    try:
        certification = CertificationService.get_certification(certification_id)
        
        if not certification:
            return jsonify({'error': 'Certification not found'}), 404
        
        CertificationService.delete_certification(certification_id)
        return jsonify({'message': 'Certification deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500