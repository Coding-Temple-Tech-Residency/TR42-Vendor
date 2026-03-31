from app.extensions import db
from app.models.base import BaseModel

class Session(BaseModel):
    __tablename__ = 'sessions'

    session_id = db.Column(db.String, primary_key=True)

    user_id = db.Column(db.String, db.ForeignKey('user.user_id'))

    is_active = db.Column(db.Boolean)


class Notification(BaseModel):
    __tablename__ = 'notification'

    notification_id = db.Column(db.String, primary_key=True)

    message = db.Column(db.Text)
    recipient = db.Column(db.String, db.ForeignKey('user.user_id'))

    level = db.Column(db.String)