from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.licenses.services.service import LicenseService
from app.blueprints.licenses.schemas import license_schema, licenses_schema


license_bp = Blueprint('licenses', __name__)



# Get all licenses
@license_bp.get('/')
def get_all_licenses():
    try:
        licenses = LicenseService.get_all_licenses()
        return jsonify(licenses_schema.dump(licenses)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific license
@license_bp.get('/<license_id>')
def get_license(license_id):
    try:
        license = LicenseService.get_license(license_id)
        
        if not license:
            return jsonify({'error': 'License not found'}), 404
        
        return jsonify(license_schema.dump(license)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new license
@license_bp.post('/')
def create_license():
    try:
        data = request.get_json()
        
        validated_data = license_schema.load(data)
        
        license = LicenseService.create_license(validated_data)
        
        return jsonify(license_schema.dump(license)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing license
@license_bp.put('/<license_id>')
def update_license(license_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = license_schema.load(data)
        
        license = LicenseService.update_license(license_id, validated_data)
        
        if not license:
            return jsonify({'error': 'License not found'}), 404
        
        
        return jsonify(license_schema.dump(license)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a certification
@license_bp.delete('/<license_id>')
def delete_license(license_id):
    try:
        license = LicenseService.get_license(license_id)
        
        if not license:
            return jsonify({'error': 'License not found'}), 404
        
        LicenseService.delete_license(license_id)
        return jsonify({'message': 'License deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500