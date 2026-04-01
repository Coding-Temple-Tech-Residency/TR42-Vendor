from app.extensions import db
from app.models.base import BaseModel

class LineItem(BaseModel):
    __tablename__ = 'line_item'

    line_item_id = db.Column(db.String, primary_key=True)
    invoice_id = db.Column(db.String, db.ForeignKey('invoice.invoice_id'))

    quantity = db.Column(db.Integer)
    rate = db.Column(db.Numeric)
    amount = db.Column(db.Numeric)

    invoice = db.relationship('Invoice', backref='line_items')


class Rating(BaseModel):
    __tablename__ = 'ratings'

    rating_id = db.Column(db.String, primary_key=True)

    contractor_id = db.Column(db.String, db.ForeignKey('contractors.contractor_id'))
    ticket_id = db.Column(db.String, db.ForeignKey('ticket.ticket_id'))

    rating = db.Column(db.Integer)
    comments = db.Column(db.Text)