from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound
from app.blueprints.invoices.services.lineitem_services import LineItemService

lineItem_bp = Blueprint('lineItem_bp', __name__)

# LineItem endpoints
@lineItem_bp.route('/line_items', methods=['GET'])
def get_line_items():
    return jsonify(LineItemService.get_all_line_items())

@lineItem_bp.route('/line_items/<string:line_item_id>', methods=['GET'])
def get_line_item(line_item_id):
    try:
        return jsonify(LineItemService.get_line_item(line_item_id))
    except NotFound as e:
        return jsonify({'error': str(e)}), 404

@lineItem_bp.route('/line_items', methods=['POST'])
def create_line_item():
    data = request.get_json()
    try:
        return jsonify(LineItemService.create_line_item(data)), 201
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400

@lineItem_bp.route('/line_items/<string:line_item_id>', methods=['DELETE'])
def delete_line_item(line_item_id):
    try:
        return LineItemService.delete_line_item(line_item_id)
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
