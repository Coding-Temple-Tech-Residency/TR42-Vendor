from app.extensions import db
from app.models.base import BaseModel

class Role(BaseModel):
    __tablename__ = 'role'

    id = db.Column(db.String, primary_key=True)

    role_name = db.Column(db.String(100))
    description = db.Column(db.Text)

    role_options = db.Column(
        db.Enum('user', 'manager', 'admin', name='role_options')
    )