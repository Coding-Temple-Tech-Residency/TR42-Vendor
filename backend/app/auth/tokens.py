from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import wraps
import os
from typing import TYPE_CHECKING

from flask import jsonify, request
from jose import jwt, exceptions as jose_exceptions

from app.blueprints.vendor_user.model import VendorUserRole

SECRET_KEY = os.environ.get("SECRET_KEY") or "super secret secrets"

if TYPE_CHECKING:
    from app.blueprints.user.model import User


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
        from app.blueprints.user.repositories.user_repositories import UserRepository

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

            if not isinstance(user_id, str):
                return jsonify({"message": "Invalid token"}), 401

            user = UserRepository.get_by_id(user_id)

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


def vendor_membership_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
            VendorUserRepository,
        )

        vendor_id = kwargs.get("vendor_id")

        if not vendor_id:
            return jsonify({"message": "vendor_id is required"}), 400

        vendor_link = VendorUserRepository.get_by_user_and_vendor(
            current_user.user_id,
            vendor_id,
        )

        if not vendor_link:
            return jsonify({"message": "User is not part of this vendor"}), 403

        return f(current_user, vendor_link, *args, **kwargs)

    return decorated


def vendor_roles_required(allowed_roles: list[VendorUserRole]):
    def decorator(f):
        @wraps(f)
        def decorated(current_user, vendor_link, *args, **kwargs):
            if vendor_link.vendor_user_role not in allowed_roles:
                return jsonify({"message": "Forbidden: insufficient vendor role"}), 403

            return f(current_user, vendor_link, *args, **kwargs)

        return decorated

    return decorator
