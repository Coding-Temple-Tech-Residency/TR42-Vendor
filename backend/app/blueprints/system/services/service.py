from app.extensions import db
from app.blueprints.system.repositories.repository import SessionRepository , NotificationRepository


class SessionService:

    @staticmethod
    def get_all_insurances():
        return SessionRepository.get_all()

    @staticmethod
    def get_insurance(session_id):
        return SessionRepository.get_by_id(session_id)

    @staticmethod
    def create_session(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_session(session_id, data):
        session = SessionRepository.get_by_id(session_id)

        if not session:
            return None

        for key, value in data.items():
            setattr(session, key, value)

        db.session.commit()
        return session

    @staticmethod
    def delete_session(session_id):
        session = SessionRepository.get_by_id(session_id)

        if not session:
            return None

        db.session.delete(session)
        db.session.commit()
        return session


class NotificationService:

    @staticmethod
    def get_all_notifications():
        return NotificationRepository.get_all()

    @staticmethod
    def get_notification(notification_id):
        return NotificationRepository.get_by_id(notification_id)

    @staticmethod
    def create_notification(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_notification(notification_id, data):
        notification = NotificationRepository.get_by_id(notification_id)

        if not notification:
            return None

        for key, value in data.items():
            setattr(notification, key, value)

        db.session.commit()
        return notification

    @staticmethod
    def delete_notification(notification_id):
        notification = NotificationRepository.get_by_id(notification_id)

        if not notification:
            return None

        db.session.delete(notification)
        db.session.commit()
        return notification