from server.app.extensions import db

class Service(db.Model):
    __tablename__ = 'service'
    
    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(80))