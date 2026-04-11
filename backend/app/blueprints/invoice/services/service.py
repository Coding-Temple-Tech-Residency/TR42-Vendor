from app.extensions import db
from app.blueprints.invoice.repositories.repository import InvoiceRepository 


class InvoiceService:

    @staticmethod
    def get_all_invoices():
        return InvoiceRepository.get_all()

    @staticmethod
    def get_invoice(invoice_id):
        return InvoiceRepository.get_by_id(invoice_id)

    @staticmethod
    def create_invoice(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_invoice(invoice_id, data):
        invoice = InvoiceRepository.get_by_id(invoice_id)

        if not invoice:
            return None

        for key, value in data.items():
            setattr(invoice, key, value)

        db.session.commit()
        return invoice

    @staticmethod
    def delete_invoice(invoice_id):
        invoice = InvoiceRepository.get_by_id(invoice_id)

        if not invoice:
            return None

        db.session.delete(invoice)
        db.session.commit()
        return invoice
