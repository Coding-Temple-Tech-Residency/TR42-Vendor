from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.invoice.services.service import InvoiceService
from app.blueprints.invoice.schemas import invoice_schema, invoices_schema


invoice_bp = Blueprint('invoices', __name__)



# Get all invoices
@invoice_bp.get('/')
def get_all_invoices():
    try:
        invoices = InvoiceService.get_all_invoices()
        return jsonify(invoices_schema.dump(invoices)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific invoice
@invoice_bp.get('/<invoice_id>')
def get_invoice(invoice_id):
    try:
        invoice = InvoiceService.get_invoice(invoice_id)
        
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        return jsonify(invoice_schema.dump(invoice)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new invoice
@invoice_bp.post('/')
def create_invoice():
    try:
        data = request.get_json()
        
        validated_data = invoice_schema.load(data)
        
        invoice = InvoiceService.create_invoice(validated_data)
        
        return jsonify(invoice_schema.dump(invoice)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing invoice
@invoice_bp.put('/<invoice_id>')
def update_invoice(invoice_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = invoice_schema.load(data)
        
        invoice = InvoiceService.update_invoice(invoice_id, validated_data)
        
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        
        return jsonify(invoice_schema.dump(invoice)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a invoice
@invoice_bp.delete('/<invoice_id>')
def delete_invoice(invoice_id):
    try:
        invoice = InvoiceService.get_invoice(invoice_id)
        
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        InvoiceService.delete_invoice(invoice_id)
        return jsonify({'message': 'Invoice deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500