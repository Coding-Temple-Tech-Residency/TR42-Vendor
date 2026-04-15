from app.extensions import db
from app.base import BaseModel

class TicketPhoto(BaseModel):
    __tablename__ = 'ticket_photos'

    id = db.Column(db.String, primary_key=True)

    ticket_id = db.Column(db.String, db.ForeignKey('ticket.id'))
    uploaded_by = db.Column(db.String, db.ForeignKey('contractors.id'))

    photo_content = db.Column(db.LargeBinary)

    ticket = db.relationship('Ticket', backref='photos')