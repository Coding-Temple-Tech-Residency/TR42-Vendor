from flask import Blueprint
from .controller import work_order_bp

def register_work_order(app):
    app.register_blueprint(work_order_bp, url_prefix='/api/work_orders')