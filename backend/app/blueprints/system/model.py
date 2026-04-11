from app.extensions import db
from datetime import datetime

class Session(db.Model):
    __tablename__ = 'sessions'

    session_id = db.Column(db.String, primary_key=True)

    user_id = db.Column(db.String, db.ForeignKey('user.user_id'))

    is_active = db.Column(db.Boolean)
    
    user_agent = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    created_by = db.Column(db.String, db.ForeignKey('user.user_id'))
    
    updated_by = db.Column(db.String, db.ForeignKey('user.user_id'))


class Notification(db.Model):
    __tablename__ = 'notification'

    notification_id = db.Column(db.String, primary_key=True)

    message = db.Column(db.Text)
    recipient = db.Column(db.String, db.ForeignKey('user.user_id'))

    level = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)