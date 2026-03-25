from flask import request, jsonify
from . import address_bp
from .model import Address
from .schemas import AddressSchema
from app.extensions import db



address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)

# GET all addresses
@address_bp.get("/")
def get_addresses():
    print("GET /addresses called")  
    addresses = Address.query.all()
    print(f" Found {len(addresses)} addresses")  
    return addresses_schema.dump(addresses), 200


# POST create new address
@address_bp.post("/")
def create_address():
    print("POST /addresses called") 
    data = request.get_json()
    print("Incoming JSON:", data)

    # Validate incoming JSON
    address_data = address_schema.load(data)
    print(" Marshmallow validated data:", address_data) 

    # Create Address instance
    new_address = Address(**address_data)
    print(" New Address object:", new_address)

    # Save to DB
    db.session.add(new_address)
    db.session.commit()
    print("Address saved to DB")  #

    return address_schema.dump(new_address), 201
