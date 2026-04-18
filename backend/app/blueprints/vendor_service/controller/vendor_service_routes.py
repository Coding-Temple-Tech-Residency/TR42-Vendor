from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from app.blueprints.vendor_service.services.vendor_service_services import VendorServiceService
from app.blueprints.vendor_service.schemas import vendor_service_schema, vendor_services_schema
from logging import getLogger

logger = getLogger(__name__)
vendor_services_bp = Blueprint("vendor_services", __name__)


"""
    Create a new vendor service.
    
    Retrieves JSON data from the request body, creates a new vendor service
    using the VendorServiceService, and returns the serialized vendor service
    object with a 201 Created HTTP status code.
    
    Returns:
        tuple: A tuple containing:
            - dict: Serialized vendor service data
            - int: HTTP status code 201 (Created)
    
    Raises:
        BadRequest: If the request body is not valid JSON or missing required fields.
    """
@vendor_services_bp.post("/")
def create_vendor_service():
    try:
        logger.info("Creating a new vendor service")
        data = request.get_json()
        logger.debug("Request data: %s", data)
        vs = VendorServiceService.create(data)
        logger.info("Vendor service created with ID: %s", vs.id)
        return vendor_service_schema.dump(vs), 201
    except Exception as e:
        logger.error("Error creating vendor service: %s", str(e))
        return {"message": str(e)}, 500
"""
    Retrieve all vendor services.

    Returns:
        tuple: A tuple containing a list of serialized vendor services and the HTTP status code 200.
    """
@vendor_services_bp.get("/")
def get_all_vendor_services():
    try:
        logger.info("Fetching all vendor services")
        vendor_services = VendorServiceService.get_all()
        logger.debug("Number of vendor services retrieved: %d", len(vendor_services))
        return vendor_services_schema.dump(vendor_services), 200
    except Exception as e:
        logger.error("Error fetching vendor services: %s", str(e))
        return {"message": "Error fetching vendor services"}, 500
    


"""
    Retrieve a VendorService by its ID.

    Args:
        vs_id (int): The unique identifier of the VendorService to retrieve.

    Returns:
        tuple: A tuple containing the serialized VendorService data and HTTP status code 200 if found,
               or a message with HTTP status code 404 if not found.
    """
@vendor_services_bp.get("/<string:vs_id>")
def get_vendor_service(vs_id):
    try:
        logger.info("Fetching vendor service with ID: %s", vs_id)
        vendor_service = VendorServiceService.get(vs_id)
        if not vendor_service:
            logger.warning("Vendor service not found with ID: %s", vs_id)
            return {"message": "VendorService not found"}, 404
        logger.debug("Vendor service retrieved: %s", vendor_service)
        return vendor_service_schema.dump(vendor_service), 200
    except Exception as e:
        logger.error("Error fetching vendor service: %s", str(e))
        return {"message": "Error fetching vendor service"}, 500
    

"""
    Retrieve all services associated with a specific vendor.
    
    Args:
        vendor_id: The unique identifier of the vendor.
    
    Returns:
        A tuple containing:
        - A list of vendor services serialized as dictionaries.
        - HTTP status code 200 (OK).
    """

@vendor_services_bp.get("/vendor/<vendor_id>")
def get_services_for_vendor(vendor_id):
    try:
        logger.info("Fetching services for vendor with ID: %s", vendor_id)
        vs = VendorServiceService.get_by_vendor(vendor_id)
        logger.debug("Number of services retrieved for vendor %s: %d", vendor_id, len(vs))
        return vendor_services_schema.dump(vs), 200
    except Exception as e:
        logger.error("Error fetching services for vendor %s: %s", vendor_id, str(e))
        return {"message": "Error fetching services for vendor"}, 500
    



"""
    Update an existing vendor service record.

    Args:
        vs_id: The unique identifier of the vendor service to update.

    Returns:
        tuple: A tuple containing:
            - dict: The serialized updated vendor service object on success,
                    or an error message dict on failure.
            - int: HTTP status code (200 for success, 404 if vendor service not found).

    Raises:
        None

    Note:
        Expects JSON request body containing the fields to update.
        Returns 404 if the vendor service with the given vs_id does not exist.
    """

@vendor_services_bp.put("/<string:vs_id>")
def update_vendor_service(vs_id):
    try:
        logger.info("Updating vendor service with ID: %s", vs_id)
        data = request.get_json()
        logger.debug("Request data for update: %s", data)
        vendor_service = VendorServiceService.get(vs_id)
        if not vendor_service:
            logger.warning("Vendor service not found with ID: %s", vs_id)
            return {"message": "VendorService not found"}, 404
        updated_vendor_service = VendorServiceService.update(vendor_service, data)
        logger.info("Vendor service updated successfully with ID: %s", vs_id)
        return vendor_service_schema.dump(updated_vendor_service), 200
    except Exception as e:
        logger.error("Error updating vendor service with ID %s: %s", vs_id, str(e))
        return {"message": "Error updating vendor service"}, 500
    
"""
    Delete a vendor service by its ID.

    Args:
        vs_id: The unique identifier of the vendor service to delete.

    Returns:
        tuple: A tuple containing:
            - dict: A response message indicating the result of the operation.
            - int: HTTP status code (200 for successful deletion, 404 if not found).

    Raises:
        None

    Example:
        >>> delete_vendor_service(123)
        ({"message": "VendorService deleted"}, 200)
        
        >>> delete_vendor_service(999)
        ({"message": "VendorService not found"}, 404)
    """

@vendor_services_bp.delete("/<string:vs_id>")
def delete_vendor_service(vs_id):
    try:
        logger.info("Deleting vendor service with ID: %s", vs_id)
        vendor_service = VendorServiceService.get(vs_id)
        if not vendor_service:
            logger.warning("Vendor service not found with ID: %s", vs_id)
            return {"message": "VendorService not found"}, 404
        VendorServiceService.delete(vendor_service)
        logger.info("Vendor service deleted successfully with ID: %s", vs_id)
        return {"message": "VendorService deleted"}, 200
    except Exception as e:
        logger.error("Error deleting vendor service with ID %s: %s", vs_id, str(e))
        return {"message": "Error deleting vendor service"}, 500
    