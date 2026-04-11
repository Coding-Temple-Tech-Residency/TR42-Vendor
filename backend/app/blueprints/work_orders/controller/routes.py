from flask import Blueprint, request, jsonify
from app.blueprints.work_orders.services.service import WorkOrderService
from app.blueprints.work_orders.schemas import WorkOrderSchema
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

work_order_bp = Blueprint('work_orders', __name__)
schema = WorkOrderSchema()
schema_many = WorkOrderSchema(many=True)

# GET all work orders
@work_order_bp.route('/', methods=['GET'])
def get_work_orders():
    try:
        work_orders = WorkOrderService.get_all_work_orders()
        result = schema_many.dump(work_orders)
        return jsonify(result), 200
    except Exception as e:
        logger.exception("Failed to fetch work orders")
        return jsonify({"error": str(e)}), 500

# GET a single work order
@work_order_bp.route('/<work_order_id>', methods=['GET'])
def get_work_order(work_order_id):
    try:
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404
        return schema.jsonify(work_order), 200
    except Exception as e:
        logger.exception(f"Failed to fetch work order {work_order_id}")
        return jsonify({"error": str(e)}), 500

# POST create a work order
@work_order_bp.route('/', methods=['POST'])
def create_work_order():
    try:
        data = request.get_json()
        work_order = WorkOrderService.create_work_order(data)
        return schema.jsonify(work_order), 201
    except Exception as e:
        logger.exception("Failed to create work order")
        return jsonify({"error": str(e)}), 500

# PUT update a work order
@work_order_bp.route('/<work_order_id>', methods=['PUT'])
def update_work_order(work_order_id):
    try:
        data = request.get_json()
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404
        updated = WorkOrderService.update_work_order(work_order, data)
        return schema.jsonify(updated), 200
    except Exception as e:
        logger.exception(f"Failed to update work order {work_order_id}")
        return jsonify({"error": str(e)}), 500

# DELETE a work order
@work_order_bp.route('/<work_order_id>', methods=['DELETE'])
def delete_work_order(work_order_id):
    try:
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404
        WorkOrderService.delete_work_order(work_order)
        return jsonify({"message": "Work order deleted"}), 200
    except Exception as e:
        logger.exception(f"Failed to delete work order {work_order_id}")
        return jsonify({"error": str(e)}), 500