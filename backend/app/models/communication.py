from server.app.extensions import db
from datetime import datetime

class Chat(db.Model):
    __tablename__ = 'chat'
    
    chat_id = db.Column(db.Integer, primary_key=True)


class Message(db.Model):
    __tablename__ = 'message'
    
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))

    chat = db.relationship('Chat', backref='messages')