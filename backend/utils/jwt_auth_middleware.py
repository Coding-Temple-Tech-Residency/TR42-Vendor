# app/utils/util.py
from datetime import datetime, timedelta, timezone
from jose import jwt, exceptions as jose_exceptions
from functools import wraps
from flask import request, jsonify
from app.models import # models to import
import os

SECRET_KEY = os.environ.get("SECRET_KEY") or "super secret secrets"
# or statement is for testing,
# github will use the or for testing purposes because it wont have the actual key


def encode_token(user_uuid, role, token_version):
    """Encode JWT using user_uuid and token_version instead of user_id"""
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
        "iat": datetime.now(timezone.utc),
        "user_uuid": str(user_uuid),
        "role": role,
        "token_version": token_version,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        parts = auth_header.split()

        if len(parts) == 0:
            return jsonify({"message": "Authorization header missing"}), 401
        elif len(parts) == 1:
            return jsonify({"message": "Bearer token missing after prefix"}), 401
        elif parts[0].lower() != "bearer":
            return (
                jsonify({"message": "Authorization header must start with 'Bearer'"}),
                401,
            )

        token = parts[1]

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_uuid = data.get("user_uuid")
            user_role = data.get("role")
            token_version = data.get("token_version", 0)

            # here we need to define roles for vendor users
            # Fetch user by role and UUID
            if user_role == #role:
                user = db.session.query(#Model).filter_by(user_uuid=user_uuid).first()
            else:
                return jsonify({"message": "Invalid role in token"}), 401

            if not user or token_version != user.token_version:
                return jsonify({"message": "Token is no longer valid"}), 401

        except jose_exceptions.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jose_exceptions.JWTError:
            return jsonify({"message": "Invalid token!"}), 401

        # Pass user object and role directly to route
        return f(user, user_role, *args, **kwargs)

    return decorated


def roles_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated(user, user_role, *args, **kwargs):  # <-- user object
            if user_role not in allowed_roles:
                return jsonify({"message": "Forbidden: insufficient role"}), 403
            return f(user, user_role, *args, **kwargs)

        return decorated

    return decorator
