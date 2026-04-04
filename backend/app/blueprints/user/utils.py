import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import current_app
from logging import getLogger

logger = getLogger(__name__)

def hash_password(password):
    logger.info("Hashing password")
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    logger.info("Verifying password")
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_token(user):
    logger.debug("Creating JWT token for user: %s", user.username)
    payload = {
        "user_id": user.user_id,
        "username": user.username,
        "is_admin": user.is_admin,
        "exp": datetime.utcnow() + timedelta(hours=8)
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")