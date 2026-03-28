from flask import Blueprint, request, jsonify

from .jwt_utils import create_jwt
from app.extensions import db

vendor_auth_bp = Blueprint("vendor_auth", __name__)


# vendor registration

@vendor_auth_bp.route("/register", methods=["POST"])
def vendor_register():
    data = request.json
    print("\n[vendor_register] Incoming data:", data)

    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    role_id = data.get("role_id")

    if not username or not password or not email or not role_id:
        return jsonify({"error": "Missing required fields"}), 400

    # 1. Fetch role_name from vendor_role
    role_query = db.text("SELECT role_name FROM vendor_role WHERE role_id = :rid")
    role_result = db.session.execute(role_query, {"rid": role_id}).fetchone()

    print("[vendor_register] Role lookup result:", role_result)

    if not role_result:
        return jsonify({"error": "Invalid role_id"}), 400

    role_name = role_result[0]
    print("[vendor_register] Role name fetched:", role_name)

    # 2. Check if username exists
    existing = db.session.execute(
        db.text("SELECT user_id FROM vendor_user WHERE username = :u"),
        {"u": username}
    ).fetchone()

    if existing:
        return jsonify({"error": "Username already taken"}), 409

    # 3. Hash password
    from werkzeug.security import generate_password_hash
    hashed_pw = generate_password_hash(password, method="pbkdf2:sha256")

    # 4. Insert vendor
    insert_query = db.text("""
        INSERT INTO vendor_user (username, password, email, role_id)
        VALUES (:username, :password, :email, :role_id)
        RETURNING user_id
    """)

    result = db.session.execute(insert_query, {
        "username": username,
        "password": hashed_pw,
        "email": email,
        "role_id": role_id
    })

    db.session.commit()

    new_user_id = result.fetchone()[0]

    return jsonify({
        "message": "Vendor registered successfully",
        "vendor": {
            "user_id": new_user_id,
            "username": username,
            "email": email,
            "role_id": role_id,
            "role_name": role_name
        }
    }), 201




#vendor login

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
