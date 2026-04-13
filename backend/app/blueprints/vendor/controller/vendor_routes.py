from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.blueprints.vendor.model import Vendor
from app.blueprints.vendor.services.vendor_services import VendorService
from app.blueprints.vendor.schemas import vendor_schema, vendors_schema
import logging

logger = logging.getLogger(__name__)


vendor_bp = Blueprint(
    "vendor_bp",
    __name__,
)


@vendor_bp.get("/")
def get_all_vendors():
    try:
        logger.debug("Fetching all vendors")
        vendor = VendorService.get_all_vendors()
        logger.info(f"Retrieved {len(vendor)} vendors")
        return vendors_schema.jsonify(vendor), 200
    except Exception:
        logger.exception("Error fetching vendors")
        return {"error": "An error occurred while fetching vendors"}, 500


@vendor_bp.post("/")
def create_vendor():
    try:
        data = request.get_json()
        logger.debug("Creating a new vendor")
        if not data:
            logger.warning("No input data provided for vendor creation")
            return {"error": "No input data provided"}, 400

        validated_data: Vendor = vendor_schema.load(data)
        logger.debug("Vendor data validated successfully")

        new_vendor: Vendor = VendorService.create_vendor(validated_data) # ran into issue here with attribute error 'dict' object has no attribute 'company_name'

        logger.info(f"Vendor created successfull: {new_vendor.company_name}")
        return vendor_schema.jsonify(new_vendor), 201
    except ValidationError as err:
        logger.warning(f"Validation error while creating vendor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
