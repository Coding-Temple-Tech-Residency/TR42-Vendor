from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import wraps
import os
from typing import TYPE_CHECKING

from flask import g, jsonify, request
from jose import jwt, exceptions as jose_exceptions

from app.blueprints.vendor_user.model import VendorUserRole

SECRET_KEY = os.environ.get("SECRET_KEY") or "super secret secrets"

if TYPE_CHECKING:
    from app.blueprints.user.model import User


def encode_token(user: User, active_vendor_id: str | None = None) -> str:
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
        "iat": datetime.now(timezone.utc),
        "user_id": user.id,
        "token_version": user.token_version,
        "is_admin": user.is_admin,
    }

    if active_vendor_id:
        payload["active_vendor_id"] = active_vendor_id

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         from app.blueprints.user.repositories.user_repositories import UserRepository
#         from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
#             VendorUserRepository,
#         )

#         auth_header = request.headers.get("Authorization", "")
#         parts = auth_header.split()

#         if len(parts) == 0:
#             return jsonify({"message": "Authorization header missing"}), 401

#         if len(parts) == 1:
#             return jsonify({"message": "Bearer token missing after prefix"}), 401

#         if parts[0].lower() != "bearer":
#             return (
#                 jsonify({"message": "Authorization header must start with 'Bearer'"}),
#                 401,
#             )

#         token = parts[1]

#         try:
#             data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#             user_id = data.get("user_id")
#             active_vendor_id = data.get("active_vendor_id")
#             token_version = data.get("token_version")

#             if not isinstance(user_id, str):
#                 return jsonify({"message": "Invalid token"}), 401

#             if not isinstance(token_version, int):
#                 return jsonify({"message": "Invalid token"}), 401

#             user = UserRepository.get_by_id(user_id)

#             if not user:
#                 return jsonify({"message": "User not found"}), 401

#             if not user.is_active:
#                 return jsonify({"message": "User account is inactive"}), 401

#             if token_version != user.token_version:
#                 return jsonify({"message": "Token is no longer valid"}), 401

#             # Store active vendor in request context for downstream decorators.
#             g.active_vendor_id = None
#             if isinstance(active_vendor_id, str) and active_vendor_id:
#                 vendor_link = VendorUserRepository.get_by_user_and_vendor(
#                     user.user_id,
#                     active_vendor_id,
#                 )
#                 if vendor_link:
#                     g.active_vendor_id = active_vendor_id

#         except jose_exceptions.ExpiredSignatureError:
#             return jsonify({"message": "Token has expired"}), 401
#         except jose_exceptions.JWTError:
#             return jsonify({"message": "Invalid token"}), 401

#         return f(user, *args, **kwargs)

#     return decorated


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from app.blueprints.user.repositories.user_repositories import UserRepository
        from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
            VendorUserRepository,
        )

        token = request.cookies.get("access_token")

        # still has auth_header logic here
        if not token:
            auth_header = request.headers.get("Authorization", "")
            parts = auth_header.split()

            if len(parts) == 2 and parts[0].lower() == "bearer":
                token = parts[1]

        if not token:
            return jsonify({"message": "Authentication token missing"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_id = data.get("user_id")
            active_vendor_id = data.get("active_vendor_id")
            token_version = data.get("token_version")

            if not isinstance(user_id, str):
                return jsonify({"message": "Invalid token"}), 401

            if not isinstance(token_version, int):
                return jsonify({"message": "Invalid token"}), 401

            user = UserRepository.get_by_id(user_id)

            if not user:
                return jsonify({"message": "User not found"}), 401

            if not user.is_active:
                return jsonify({"message": "User account is inactive"}), 401

            if token_version != user.token_version:
                return jsonify({"message": "Token is no longer valid"}), 401

            g.active_vendor_id = None
            if isinstance(active_vendor_id, str) and active_vendor_id:
                vendor_link = VendorUserRepository.get_by_user_and_vendor(
                    user.id,
                    active_vendor_id,
                )
                if vendor_link:
                    g.active_vendor_id = active_vendor_id

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
            vendor_id = kwargs.get(
                "id"
            )  # fallback to 'id' if 'vendor_id' is not present

        if not vendor_id:
            vendor_id = request.args.get("vendor_id")

        if not vendor_id:
            body = request.get_json(silent=True) or {}
            vendor_id = body.get("vendor_id")

        if not vendor_id:
            vendor_id = getattr(g, "active_vendor_id", None)

        if not vendor_id:
            return jsonify({"message": "Vendor ID is required"}), 400

        vendor_link = VendorUserRepository.get_by_user_and_vendor(
            current_user.id,
            vendor_id,
        )

        if not vendor_link:
            return jsonify({"message": "User is not part of this vendor"}), 403

        kwargs["vendor_id"] = (
            vendor_id  # ensure vendor_id is in kwargs for downstream use
        )
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
