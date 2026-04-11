from app.blueprints.invoice.model import Invoice
from app.extensions import db

class InvoiceRepository:
    
    @staticmethod
    def get_all():
        return Invoice.query.all()
    
    @staticmethod
    def get_by_id(invoice_id):
        return Invoice.query.get(invoice_id)
    
    @staticmethod
    def create(invoice):
        db.session.add(invoice)
        db.session.commit()
        return invoice
    
    @staticmethod
    def update(invoice):
        db.session.commit()
        return invoice
    
    @staticmethod
    def delete(invoice):
        db.session.delete(invoice)
        db.session.commit()