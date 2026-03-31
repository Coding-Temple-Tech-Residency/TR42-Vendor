import re
from marshmallow import ValidationError
from datetime import datetime, timezone

PHONE_REGEX = re.compile(r"^\d{3}-\d{3}-\d{4}$")
ADDRESS_REGEX = re.compile(r"^[A-Za-z0-9\s.'#,-]{5,120}$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def strip_strings(data):
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.strip()
    return data


def strip_input(data, **kwargs):
    return strip_strings(data)


def validate_name(value, min_length=2, field_name="Name"):
    if not value or len(value.strip()) < min_length:
        raise ValidationError(
            f"{field_name} must be at least {min_length} characters long"
        )


def validate_address(value, **kwargs):
    if not ADDRESS_REGEX.match(value):
        raise ValidationError("Enter a valid street address (e.g., '123 Main St')")


def validate_password(value, **kwargs):
    if not value or len(value) < 8:
        raise ValidationError("Password must be longer than 8 characters.")


def validate_email_format(value, **kwargs):
    if not EMAIL_REGEX.match(value):
        raise ValidationError(
            "Invalid email address, must be in format: user@example.com"
        )


def validate_phone_format(value, **kwargs):
    if not PHONE_REGEX.match(value):
        raise ValidationError("Invalid phone number format (XXX-XXX-XXXX)")


def utc_now():
    return datetime.now(timezone.utc)
