from flask import Blueprint
from .controller import contractor_bp

def register_contractor(app):
    app.register_blueprint(contractor_bp, url_prefix='/api/contractors')