from app.extensions import ma
from app.models.system import Session, Notification


class SessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Session
        load_instance = True


session_schema = SessionSchema()
sessions_schema = SessionSchema(many=True)

class NotificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Notification
        load_instance = True


notification_schema = NotificationSchema()
notifications_schema = NotificationSchema(many=True)