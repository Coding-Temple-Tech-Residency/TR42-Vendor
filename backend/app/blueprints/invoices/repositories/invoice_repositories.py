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

class LineItemRepository:
    @staticmethod
    def get_by_id(line_item_id: str):
        return db.session.get(LineItem, line_item_id)

    @staticmethod
    def get_all():
        return db.session.scalars(select(LineItem)).all()

    @staticmethod
    def create(line_item: LineItem):
        db.session.add(line_item)
        db.session.commit()
        return line_item

    @staticmethod
    def delete(line_item: LineItem):
        db.session.delete(line_item)
        db.session.commit()
