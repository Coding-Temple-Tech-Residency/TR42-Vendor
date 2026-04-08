from sqlalchemy import select
from app.extensions import db
from app.blueprints.invoices.model import Invoice, LineItem
from logging import getLogger

logger = getLogger(__name__)

class InvoiceRepository:
    @staticmethod
    def get_by_id(invoice_id: str):
        return db.session.get(Invoice, invoice_id)

    @staticmethod
    def get_all():
        return db.session.scalars(select(Invoice)).all()

    @staticmethod
    def create(invoice: Invoice):
        db.session.add(invoice)
        db.session.commit()
        return invoice

    @staticmethod
    def delete(invoice: Invoice):
        db.session.delete(invoice)
        db.session.commit()
