import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    #SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@127.0.0.1:5432/mydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False