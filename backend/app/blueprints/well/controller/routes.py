from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.well.services.service import WellService
from app.blueprints.well.schemas import well_schema, wells_schema


well_bp = Blueprint('well', __name__)



# Get all wells
@well_bp.get('/')
def get_all_wells():
    try:
        wells = WellService.get_all_wells()
        return jsonify(wells_schema.dump(wells)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific well
@well_bp.get('/<well_id>')
def get_well(well_id):
    try:
        well = WellService.get_well(well_id)
        
        if not well:
            return jsonify({'error': 'Well not found'}), 404
        
        return jsonify(well_schema.dump(well)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new well
@well_bp.post('/')
def create_well():
    try:
        data = request.get_json()
        
        validated_data = well_schema.load(data)
        
        well = WellService.create_well(validated_data)
        
        return jsonify(well_schema.dump(well)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing well
@well_bp.put('/<well_id>')
def update_well(well_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = well_schema.load(data)
        
        well = WellService.update_well(well_id, validated_data)
        
        if not well:
            return jsonify({'error': 'Well not found'}), 404
        
        
        return jsonify(well_schema.dump(well)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a well
@well_bp.delete('/<well_id>')
def delete_well(well_id):
    try:
        well = WellService.get_well(well_id)
        
        if not well:
            return jsonify({'error': 'Well not found'}), 404
        
        WellService.delete_well(well_id)
        return jsonify({'message': 'Well deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500