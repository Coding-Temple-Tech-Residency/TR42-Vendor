from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound
from app.blueprints.invoices.services.invoice_services import InvoiceService

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