from functools import wraps
from flask import request, jsonify
from .jwt_utils import decode_jwt
from app.extensions import db

def vendor_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        #  Read Authorization header

        auth_header = request.headers.get("Authorization")
        print("\n[vendor_required] Authorization header:", auth_header)

        if not auth_header or not auth_header.startswith("Bearer "):
            print("[vendor_required] Missing or malformed Authorization header")
            return jsonify({"error": "Missing token"}), 401

#  Extract token

        token = auth_header.split(" ")[1]
        print("[vendor_required] Extracted token:", token)
        payload = decode_jwt(token)

       #  Decode token

        if not payload:
            print("[vendor_required] Token invalid or expired")
            return jsonify({"error": "Invalid or expired token"}), 401

      #Check user type
        if payload.get("type") != "vendor":
            return jsonify({"error": "Vendor access only"}), 403

        # verify vendor_user exists using SQLAlchemy

        result = db.session.execute(
            db.text("SELECT user_id FROM vendor_user WHERE user_id = :uid"),
            {"uid": payload["user_id"]}
        ).fetchone()
        print("[vendor_required] DB lookup result:", result)

        if not result:
            print("[vendor_required] Vendor not found in DB")
            return jsonify({"error": "Vendor not found"}), 403
       
       #  Success
        print("[vendor_required] Vendor validated successfully\n")
        request.vendor = payload
        return f(*args, **kwargs)

    return wrapper
