from app.extensions import db
from app.models.base import BaseModel

class Chat(BaseModel):
    __tablename__ = 'chat'

    chat_id = db.Column(db.String, primary_key=True)


class Message(BaseModel):
    __tablename__ = 'messages'

    message_id = db.Column(db.String, primary_key=True)

    sender = db.Column(db.String, db.ForeignKey('user.user_id'))
    recipient = db.Column(db.String, db.ForeignKey('user.user_id'))
    chat_id = db.Column(db.String, db.ForeignKey('chat.chat_id'))

    message = db.Column(db.Text)

    chat = db.relationship('Chat', backref='messages')