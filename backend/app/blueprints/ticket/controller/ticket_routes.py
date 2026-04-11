from flask import Blueprint, request, jsonify
from app.blueprints.ticket.services.service import TicketService
from app.blueprints.ticket.schemas import TicketSchema
import logging


ticket_bp = Blueprint('tickets', __name__)


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ticket_bp = Blueprint('tickets', __name__)
schema = TicketSchema()
schema_many = TicketSchema(many=True)

# GET all tickets
@ticket_bp.route('/', methods=['GET'])
def get_tickets():
    try:
        tickets = TicketService.get_all_tickets()
        return jsonify(schema_many.dump(tickets)), 200
    except Exception as e:
        logger.exception("Failed to fetch tickets")
        return jsonify({"error": str(e)}), 500

# GET single ticket
@ticket_bp.route('/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    try:
        ticket = TicketService.get_ticket(ticket_id)
        if not ticket:
            return jsonify({"error": "Ticket not found"}), 404
        return schema.jsonify(ticket), 200
    except Exception as e:
        logger.exception(f"Failed to fetch ticket {ticket_id}")
        return jsonify({"error": str(e)}), 500

# POST create ticket
@ticket_bp.route('/', methods=['POST'])
def create_ticket():
    try:
        data = request.get_json()
        ticket = TicketService.create_ticket(data)
        return schema.jsonify(ticket), 201
    except Exception as e:
        logger.exception("Failed to create ticket")
        return jsonify({"error": str(e)}), 500

# PUT update ticket
@ticket_bp.route('/<ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    try:
        data = request.get_json()
        ticket = TicketService.get_ticket(ticket_id)
        if not ticket:
            return jsonify({"error": "Ticket not found"}), 404
        updated = TicketService.update_ticket(ticket, data)
        return schema.jsonify(updated), 200
    except Exception as e:
        logger.exception(f"Failed to update ticket {ticket_id}")
        return jsonify({"error": str(e)}), 500

# DELETE ticket
@ticket_bp.route('/<ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        ticket = TicketService.get_ticket(ticket_id)
        if not ticket:
            return jsonify({"error": "Ticket not found"}), 404
        TicketService.delete_ticket(ticket)
        return jsonify({"message": "Ticket deleted"}), 200
    except Exception as e:
        logger.exception(f"Failed to delete ticket {ticket_id}")
        return jsonify({"error": str(e)}), 500