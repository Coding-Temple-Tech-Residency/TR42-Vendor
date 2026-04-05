from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import wraps
import os
from typing import TYPE_CHECKING

from flask import jsonify, request
from jose import jwt, exceptions as jose_exceptions
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

SECRET_KEY = os.environ.get("SECRET_KEY") or "super secret secrets"

if TYPE_CHECKING:
    from app.blueprints.user.model import User


def hash_password(raw_password: str) -> str:
    return generate_password_hash(raw_password)


def verify_password(raw_password: str, password_hash: str) -> bool:
    return check_password_hash(password_hash, raw_password)


def encode_token(user: User) -> str:
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
        "iat": datetime.now(timezone.utc),
        "user_id": user.user_id,
        "token_version": user.token_version,
        "is_admin": user.is_admin,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from app.blueprints.user.model import User

        auth_header = request.headers.get("Authorization", "")
        parts = auth_header.split()

        if len(parts) == 0:
            return jsonify({"message": "Authorization header missing"}), 401

        if len(parts) == 1:
            return jsonify({"message": "Bearer token missing after prefix"}), 401

        if parts[0].lower() != "bearer":
            return (
                jsonify({"message": "Authorization header must start with 'Bearer'"}),
                401,
            )

        token = parts[1]

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_id = data.get("user_id")
            token_version = data.get("token_version", 0)

            user = db.session.query(User).filter_by(user_id=user_id).first()

            if not user:
                return jsonify({"message": "User not found"}), 401

            if not user.is_active:
                return jsonify({"message": "User account is inactive"}), 401

            if token_version != user.token_version:
                return jsonify({"message": "Token is no longer valid"}), 401

        except jose_exceptions.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except jose_exceptions.JWTError:
            return jsonify({"message": "Invalid token"}), 401

        return f(user, *args, **kwargs)

    return decorated
