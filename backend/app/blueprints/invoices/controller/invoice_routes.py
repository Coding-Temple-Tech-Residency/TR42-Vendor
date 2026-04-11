from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound
from app.blueprints.invoices.services.invoice_services import InvoiceService
from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
import logging 
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

invoice_bp = Blueprint('invoice_bp', __name__)

@invoice_bp.route('/invoices', methods=['GET'])
def get_invoices():
    return jsonify(InvoiceService.get_all_invoices())

@invoice_bp.route('/invoices/<string:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    try:
        return jsonify(InvoiceService.get_invoice(invoice_id))
    except NotFound as e:
        return jsonify({'error': str(e)}), 404

@invoice_bp.route('/invoices', methods=['POST'])
def create_invoice():
    data = request.get_json()
    try:
        return jsonify(InvoiceService.create_invoice(data)), 201
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400

@invoice_bp.route('/invoices/<string:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    try:
        return InvoiceService.delete_invoice(invoice_id)
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    
# Get all work orders assigned to current vendor
@invoice_bp.route('/vendor/<vendor_id>', methods=['GET'])
@token_required
@vendor_membership_required
@vendor_roles_required(['admin', 'manager'])
def get_vendor_invoices(current_user, vendor_link, vendor_id):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    try:
        result = InvoiceService.get_vendor_invoices_paginated(
            vendor_id=vendor_id,
            page=page,
            per_page=per_page,
        )
        return jsonify(result), 200
    except Exception as e:
        logger.exception(f"Failed to fetch work orders for vendor {vendor_id}")
        return jsonify({"error": str(e)}), 500
