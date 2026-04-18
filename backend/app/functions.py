import re
from marshmallow import ValidationError
from datetime import datetime, timezone
import uuid

PHONE_REGEX = re.compile(r"^\d{3}-\d{3}-\d{4}$")
ADDRESS_REGEX = re.compile(r"^[A-Za-z0-9\s.'#,-]{5,120}$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
PASSWORD_REGEX = re.compile(
    r"""
    ^(?=.*[a-z])              # lowercase
    (?=.*[A-Z])               # uppercase
    (?=.*\d)                  # digit
    (?=.*[^A-Za-z0-9])        # special char
    (?!.*(.)\1{2,})           # no 3 repeating chars
    .{12,}$                   # min length 12
    """,
    re.VERBOSE,
)
CITY_REGEX = re.compile(r"^[A-Za-z\s.'-]{2,50}$")
STATE_REGEX = re.compile(r"^[A-Z]{2}$")
ZIP_REGEX = re.compile(r"^\d{5}(-\d{4})?$")


def strip_strings(value):
    if isinstance(value, dict):
        return {k: strip_strings(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [strip_strings(item) for item in value]
    elif isinstance(value, str):
        return value.strip()
    return value


def strip_input(data, **kwargs):
    return strip_strings(data)


def validate_name(value, min_length=2, field_name="Name"):
    if not value or len(value.strip()) < min_length:
        raise ValidationError(
            f"{field_name} must be at least {min_length} characters long"
        )


def validate_street(value, **kwargs):
    if not ADDRESS_REGEX.fullmatch(value):
        raise ValidationError("Enter a valid street address (e.g., '123 Main St')")


def validate_password(value: str) -> None:
    if not value:
        raise ValidationError("Password is required.")

    if not PASSWORD_REGEX.fullmatch(value):
        raise ValidationError(
            "Password must be at least 12 characters long and include uppercase, lowercase, number, and special character, "
            "and must not contain more than 2 identical characters in a row."
        )


def validate_email_format(value, **kwargs):
    if not EMAIL_REGEX.fullmatch(value):
        raise ValidationError(
            "Invalid email address, must be in format: user@example.com"
        )


def validate_phone_format(value, **kwargs):
    if not PHONE_REGEX.fullmatch(value):
        raise ValidationError("Invalid phone number format (XXX-XXX-XXXX)")


def validate_city(value):
    if not CITY_REGEX.fullmatch(value.strip()):
        raise ValidationError("Enter a valid city.")


def validate_state(value):
    if not STATE_REGEX.fullmatch(value.strip().upper()):
        raise ValidationError("Enter a valid 2-letter state code.")


def validate_zipcode(value):
    if not ZIP_REGEX.fullmatch(value.strip()):
        raise ValidationError("Enter a valid ZIP code.")


def validate_password_content(data):
    password = data.get("password", "")
    username = data.get("username", "")
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")

    password_lower = password.lower()

    for label, field_value in {
        "username": username,
        "first name": first_name,
        "last name": last_name,
    }.items():
        cleaned = (field_value or "").strip().lower()
        if len(cleaned) >= 4 and cleaned in password_lower:
            raise ValidationError(
                {"password": [f"Password must not contain the user's {label}."]}
            )


def utc_now():
    return datetime.now(timezone.utc)


def generate_uuid():
    return str(uuid.uuid4())
