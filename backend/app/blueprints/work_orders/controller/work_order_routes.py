from flask import Blueprint, request, jsonify
from app.blueprints.work_orders.services.service import WorkOrderService
from app.blueprints.work_orders.schemas import work_order_schema, work_orders_schema
from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

work_order_bp = Blueprint('work_orders', __name__)

# GET all work orders
@work_order_bp.route('/', methods=['GET'])
@token_required
@vendor_roles_required(['admin'])
def get_work_orders():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    try:
        result = WorkOrderService.get_all_work_orders_paginated(page=page, per_page=per_page)
        return jsonify(result), 200
    except Exception as e:
        logger.exception("Failed to fetch work orders")
        return jsonify({"error": str(e)}), 500

# GET a single work order
@work_order_bp.route('/<work_order_id>', methods=['GET'])
@token_required
@vendor_roles_required(['admin'])
def get_work_order(work_order_id):
    try:
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404
        return work_order_schema.jsonify(work_order), 200
    except Exception as e:
        logger.exception(f"Failed to fetch work order {work_order_id}")
        return jsonify({"error": str(e)}), 500
    
# Get all work orders assigned to current vendor
@work_order_bp.route('/vendor/<vendor_id>', methods=['GET'])
@token_required
@vendor_membership_required
@vendor_roles_required(['admin', 'manager'])
def get_vendor_work_orders(current_user, vendor_link, vendor_id):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    try:
        result = WorkOrderService.get_vendor_work_orders_paginated(
            vendor_id=vendor_id,
            page=page,
            per_page=per_page,
        )
        return jsonify(result), 200
    except Exception as e:
        logger.exception(f"Failed to fetch work orders for vendor {vendor_id}")
        return jsonify({"error": str(e)}), 500

# POST create a work order
@work_order_bp.route('/', methods=['POST'])
@token_required
@vendor_roles_required(['admin'])
def create_work_order():
    try:
        data = request.get_json()
        work_order = WorkOrderService.create_work_order(data)
        return work_order_schema.jsonify(work_order), 201
    except Exception as e:
        logger.exception("Failed to create work order")
        return jsonify({"error": str(e)}), 500

# PUT update a work order
@work_order_bp.route('/<work_order_id>', methods=['PUT'])
@token_required
@vendor_membership_required
@vendor_roles_required(['admin', 'manager'])
def update_work_order(work_order_id):
    try:
        data = request.get_json()
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404
        updated = WorkOrderService.update_work_order(work_order, data)
        return work_order_schema.jsonify(updated), 200
    except Exception as e:
        logger.exception(f"Failed to update work order {work_order_id}")
        return jsonify({"error": str(e)}), 500

# DELETE a work order
@work_order_bp.route('/<work_order_id>', methods=['DELETE'])
@token_required
@vendor_membership_required
@vendor_roles_required(['admin', 'manager'])
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