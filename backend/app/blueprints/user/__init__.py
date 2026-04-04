
from flask import Blueprint
from .controller import user_bp

def register_user(app):
    app.register_blueprint(user_bp, url_prefix='/api/userss')