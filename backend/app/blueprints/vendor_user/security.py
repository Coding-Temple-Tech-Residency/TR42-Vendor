from functools import wraps

from flask import jsonify

from app.blueprints.vendor_user.model import VendorUserRole


def vendor_roles_required(allowed_roles: list[VendorUserRole]):
    def decorator(f):
        @wraps(f)
        def decorated(current_user, vendor_link, *args, **kwargs):
            if vendor_link.role not in allowed_roles:
                return jsonify({"message": "Forbidden: insufficient vendor role"}), 403

            return f(current_user, vendor_link, *args, **kwargs)

        return decorated

    return decorator
