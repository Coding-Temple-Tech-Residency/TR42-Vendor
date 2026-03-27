import jwt
import datetime

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_jwt(payload: dict, expires_in_minutes=60):
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in_minutes)
    print("\n[create_jwt] Payload before encoding:", payload)

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print("[create_jwt] Generated token:", token, "\n")
    
    return token

def decode_jwt(token: str):
    print("\n[decode_jwt] Incoming token:", token)
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("[decode_jwt] Decoded payload:", decoded, "\n")
        return decoded
    except jwt.ExpiredSignatureError:
        print("[decode_jwt] ERROR: Token expired\n")
        return None
    except jwt.InvalidTokenError as e:
        print("[decode_jwt] ERROR: Invalid token:", str(e), "\n")
        return None
