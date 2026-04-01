#This removes duplicate fields across every table
from app.extensions import db
from sqlalchemy.sql import func

class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    created_by = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String, db.ForeignKey('user.user_id'))