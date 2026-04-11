from app.blueprints.system.model import Session, Notification
from app.extensions import db

class SessionRepository:
    
    @staticmethod
    def get_all():
        return Session.query.all()
    
    @staticmethod
    def get_by_id(session_id):
        return Session.query.get(session_id)
    
    @staticmethod
    def create(session):
        db.session.add(session)
        db.session.commit()
        return session
    
    @staticmethod
    def update(session):
        db.session.commit()
        return session
    
    @staticmethod
    def delete(session):
        db.session.delete(session)
        db.session.commit()
        
        
class NotificationRepository:
    
    @staticmethod
    def get_all():
        return Notification.query.all()
    
    @staticmethod
    def get_by_id(notification_id):
        return Notification.query.get(notification_id)
    
    @staticmethod
    def create(notification):
        db.session.add(notification)
        db.session.commit()
        return notification
    
    @staticmethod
    def update(notification):
        db.session.commit()
        return notification
    
    @staticmethod
    def delete(notification):
        db.session.delete(notification)
        db.session.commit()