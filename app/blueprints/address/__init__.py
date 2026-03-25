from flask import Blueprint

address_bp = Blueprint("address", __name__)
from . import routes
