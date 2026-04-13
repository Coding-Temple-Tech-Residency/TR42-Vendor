from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.work_order_extras.services.service import CancelledWorkOrderService
from app.blueprints.work_order_extras.schemas import cancelled_work_order_schema, cancelled_work_orders_schema


cancelled_work_order_bp = Blueprint('cancelled_work_order', __name__)



# Get all cancelled work orders
@cancelled_work_order_bp.get('/')
def get_all_cancelled_work_orders():
    try:
        cancelled_work_orders = CancelledWorkOrderService.get_all_cancelled_work_orders()
        return jsonify(cancelled_work_orders_schema.dump(cancelled_work_orders)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific cancelled work order
@cancelled_work_order_bp.get('/<cancelled_work_order_id>')
def get_cancelled_work_order(cancelled_work_order_id):
    try:
        cancelled_work_order = CancelledWorkOrderService.get_cancelled_work_order(cancelled_work_order_id)
        
        if not cancelled_work_order:
            return jsonify({'error': 'Cancelled work order not found'}), 404
        
        return jsonify(cancelled_work_order_schema.dump(cancelled_work_order)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new cancelled work order
@cancelled_work_order_bp.post('/')
def create_cancelled_work_order():
    try:
        data = request.get_json()
        
        validated_data = cancelled_work_order_schema.load(data)
        
        cancelled_work_order = CancelledWorkOrderService.create_cancelled_work_order(validated_data)
        
        return jsonify(cancelled_work_order_schema.dump(cancelled_work_order)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing cancelled work order
@cancelled_work_order_bp.put('/<cancelled_work_order_id>')
def update_cancelled_work_order(cancelled_work_order_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = cancelled_work_order_schema.load(data)
        
        cancelled_work_order = CancelledWorkOrderService.update_cancelled_work_order(cancelled_work_order_id, validated_data)
        
        if not cancelled_work_order:
            return jsonify({'error': 'Cancelled work order not found'}), 404
        
        
        return jsonify(cancelled_work_order_schema.dump(cancelled_work_order)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a cancelled work order
@cancelled_work_order_bp.delete('/<cancelled_work_order_id>')
def delete_cancelled_work_order(cancelled_work_order_id):
    try:
        cancelled_work_order = CancelledWorkOrderService.get_cancelled_work_order(cancelled_work_order_id)
        
        if not cancelled_work_order:
            return jsonify({'error': 'Cancelled work order not found'}), 404
        
        CancelledWorkOrderService.delete_cancelled_work_order(cancelled_work_order_id)
        return jsonify({'message': 'Cancelled work order deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500