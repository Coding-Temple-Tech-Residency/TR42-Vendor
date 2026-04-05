from app.extensions import db
from app.base import BaseModel

class User(BaseModel):
    __tablename__ = 'user'

    user_id = db.Column(db.String, primary_key=True)

    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)

    token_version = db.Column(db.Integer, default=0)

    type = db.Column(db.Enum('operator', 'vendor', 'contractor', name='user_type'), nullable=False)

    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)