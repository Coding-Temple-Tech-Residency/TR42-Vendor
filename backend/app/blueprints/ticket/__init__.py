from flask import Blueprint
from .controller import ticket_bp

def register_ticket(app):
    app.register_blueprint(ticket_bp, url_prefix='/api/tickets')