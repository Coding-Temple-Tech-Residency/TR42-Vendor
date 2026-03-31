from server.app.extensions import db
from datetime import datetime

class Client(db.Model):
    __tablename__ = 'client'
    
    client_id = db.Column(db.Integer, primary_key=True)
    client_company_name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    client_status = db.Column(db.String(20), nullable=False)
    client_code = db.Column(db.String(20), unique=True, nullable=False)