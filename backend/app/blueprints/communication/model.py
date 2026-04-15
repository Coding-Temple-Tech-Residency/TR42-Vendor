from app.extensions import db
from app.base import BaseModel

class Chat(BaseModel):
    __tablename__ = 'chat'

    id = db.Column(db.String, primary_key=True)


class Message(BaseModel):
    __tablename__ = 'messages'

    id = db.Column(db.String, primary_key=True)

    sender = db.Column(db.String, db.ForeignKey('user.id'))
    recipient = db.Column(db.String, db.ForeignKey('user.id'))
    chat_id = db.Column(db.String, db.ForeignKey('chat.id'))

    message = db.Column(db.Text)

    chat = db.relationship('Chat', backref='messages')