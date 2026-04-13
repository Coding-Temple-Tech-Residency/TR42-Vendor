from sqlalchemy import Integer
from datetime import datetime
from sqlalchemy import ForeignKey, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel


class Chat(BaseModel):
    __tablename__ = 'chat'

    chat_id : Mapped[str] = mapped_column(String, primary_key=True)


class Message(BaseModel):
    __tablename__ = 'messages'

    message_id : Mapped[str] = mapped_column(String, primary_key=True)

    sender : Mapped[str] = mapped_column(String, ForeignKey('user.user_id'))
    recipient : Mapped[str] = mapped_column(String, ForeignKey('user.user_id'))
    chat_id : Mapped[str] = mapped_column(String, ForeignKey('chat.chat_id'))

    message : Mapped[str] = mapped_column(String)

    chat : Mapped['Chat'] = relationship('Chat', backref='messages')