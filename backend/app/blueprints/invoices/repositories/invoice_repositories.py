from sqlalchemy import select, desc
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

    @staticmethod
    def get_all_paginated(page: int = 1, per_page: int = 10) -> dict:
        query = Invoice.query.order_by(desc(Invoice.created_at))
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            'invoices': pagination.items,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': pagination.page,
            'per_page': pagination.per_page,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev,
            'next_page': pagination.next_num if pagination.has_next else None,
            'prev_page': pagination.prev_num if pagination.has_prev else None
        }