from app.base import BaseModel
from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column



class Session(BaseModel):
    __tablename__ = 'sessions'

    session_id : Mapped [str] = mapped_column(String, primary_key=True)

    user_id : Mapped [str] = mapped_column(String, ForeignKey('user.user_id'))

    is_active : Mapped[bool] = mapped_column(Boolean)
    
    user_agent : Mapped [str] = mapped_column(String)
    


class Notification(BaseModel):
    __tablename__ = 'notification'

    notification_id : Mapped [str] = mapped_column(String, primary_key=True)

    message : Mapped [str] = mapped_column(String)
    recipient : Mapped [str] = mapped_column(String, ForeignKey('user.user_id'))

    level : Mapped [str] = mapped_column(String)
