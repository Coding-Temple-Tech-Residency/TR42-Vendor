from flask import Blueprint, request, jsonify
from app.blueprints.work_orders.services.services import WorkOrderService
from app.blueprints.work_orders.schemas import work_order_schema, work_orders_schema
from app.blueprints.vendor_user.model import VendorUserRole
from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from werkzeug.exceptions import BadRequest, Forbidden
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

work_order_bp = Blueprint('work_orders', __name__)

# GET all work orders for a vendor with pagination
         # Need to create a basic role restriciton so a super can see all work orders, but a manager or admin can only see work orders for their vendor. 
         # This will be done in the service layer, but we need to pass the current user and vendor link to the service layer.
@work_order_bp.route('/', methods=['GET'])
@token_required
# @vendor_membership_required
# @vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_work_orders(current_user):
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
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_work_order(current_user, vendor_link, vendor_id, work_order_id):
    try:
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404

        if work_order.assigned_vendor != vendor_id:
            return jsonify({"error": "Work order is not assigned to your active vendor"}), 403

        return work_order_schema.jsonify(work_order), 200
    except Exception as e:
        logger.exception(f"Failed to fetch work order {work_order_id}")
        return jsonify({"error": str(e)}), 500
    
# Get all work orders assigned to current vendor with optional status filter
# {{baseUrl}}/api/work_orders/vendor?status={{status}}&page={{page}}&per_page={{per_page}}
# Optional override: ?vendor_id={{vendorId}}
@work_order_bp.route('/vendor', methods=['GET'])
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_vendor_work_orders(current_user, vendor_link, vendor_id):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    status = request.args.get("status", default="all")

    try:
        result = WorkOrderService.get_vendor_work_orders_paginated(
            vendor_id=vendor_id,
            status=status,
            page=page,
            per_page=per_page
        )
        return jsonify(result), 200
    except Exception as e:
        logger.exception(f"Failed to fetch work orders for vendor {vendor_id}")
        return jsonify({"error": str(e)}), 500

# POST create a work order
@work_order_bp.route('/', methods=['POST'])
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def create_work_order(current_user, vendor_link, vendor_id):
    try:
        data = request.get_json() or {}

        # Keep creation scoped to the active vendor context.
        if data.get("assigned_vendor") in (None, ""):
            data["assigned_vendor"] = vendor_id
        elif data.get("assigned_vendor") != vendor_id:
            raise Forbidden("assigned_vendor must match your active vendor")

        work_order = WorkOrderService.create_work_order(data)
        return work_order_schema.jsonify(work_order), 201
    except Forbidden as e:
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.exception("Failed to create work order")
        return jsonify({"error": str(e)}), 500

# PUT update a work order
@work_order_bp.route('/<work_order_id>', methods=['PUT'])
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def update_work_order(current_user, vendor_link, vendor_id, work_order_id):
    try:
        data = request.get_json() or {}
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404

        if work_order.assigned_vendor != vendor_id:
            return jsonify({"error": "Work order is not assigned to your active vendor"}), 403

        if data.get("assigned_vendor") not in (None, "", vendor_id):
            raise Forbidden("assigned_vendor must match your active vendor")

        if data.get("assigned_vendor") in (None, ""):
            data["assigned_vendor"] = vendor_id

        updated = WorkOrderService.update_work_order(work_order, data)
        return work_order_schema.jsonify(updated), 200
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Forbidden as e:
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.exception(f"Failed to update work order {work_order_id}")
        return jsonify({"error": str(e)}), 500

# DELETE a work order
@work_order_bp.route('/<work_order_id>', methods=['DELETE'])
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN])
def delete_work_order(current_user, vendor_link, vendor_id, work_order_id):
    try:
        work_order = WorkOrderService.get_work_order(work_order_id)
        if not work_order:
            return jsonify({"error": "Work order not found"}), 404

        if work_order.assigned_vendor != vendor_id:
            return jsonify({"error": "Work order is not assigned to your active vendor"}), 403

        WorkOrderService.delete_work_order(work_order)
        return jsonify({"message": "Work order deleted"}), 200
    except Exception as e:
        logger.exception(f"Failed to delete work order {work_order_id}")
        return jsonify({"error": str(e)}), 500