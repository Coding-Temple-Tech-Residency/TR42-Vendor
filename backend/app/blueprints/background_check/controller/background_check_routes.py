from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.background_check.services.service import BackgroundCheckService
from app.blueprints.background_check.schemas import background_check_schema, background_checks_schema


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