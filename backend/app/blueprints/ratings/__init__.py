from flask import Blueprint
from .controller import ratings_bp

def register_rating(app):
    app.register_blueprint(ratings_bp, url_prefix='/api/ratings')