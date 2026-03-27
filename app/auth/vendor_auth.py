from flask import Blueprint, request, jsonify
#from werkzeug.security import check_password_hash
from .jwt_utils import create_jwt
from app.extensions import db

vendor_auth_bp = Blueprint("vendor_auth", __name__)


@vendor_auth_bp.route("/login", methods=["POST"])
def vendor_login():
    data = request.json
    print("\n[vendor_login] Incoming request data:", data)
    username = data.get("username")
    password = data.get("password")


 # Query vendor_user + vendor_role using SQLAlchemy
    query = db.text("""
        SELECT vu.user_id, vu.username, vu.password, vu.email, vr.role_name
        FROM vendor_user vu
        JOIN vendor_role vr ON vu.role_id = vr.role_id
        WHERE vu.username = :username
    """)

    result = db.session.execute(query, {"username": username}).fetchone()
    print("[vendor_login] DB query result:", result)

    if not result:
        print("[vendor_login] ERROR: Username not found\n")
        return jsonify({"error": "Invalid username"}), 401

    user_id, username, hashed_pw, email, role_name = result
    print("[vendor_login] Extracted fields:",
          "\n  user_id:", user_id,
          "\n  username:", username,
          "\n  email:", email,
          "\n  role:", role_name)

    #if not check_password_hash(hashed_pw, password):
       # return jsonify({"error": "Invalid password"}), 401


    # Build JWT payload
    payload = {
        "user_id": user_id,
        "username": username,
        "email": email,
        "role": role_name,
        "type": "vendor"
    }
    print("[vendor_login] JWT payload before encoding:", payload)

    token = create_jwt(payload)
    print("[vendor_login] Generated JWT token:", token, "\n")

    return jsonify({
        "message": "Vendor authenticated",
        "token": token,
        "vendor": {
            "user_id": user_id,
            "username": username,
            "email": email,
            "role": role_name
        }
    })
