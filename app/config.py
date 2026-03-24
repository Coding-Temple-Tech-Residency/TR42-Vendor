import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@127.0.0.1:5432/mydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
