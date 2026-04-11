from app.blueprints.invoices.repositories.invoice_repositories import InvoiceRepository
from app.blueprints.invoices.model import Invoice
from app.blueprints.invoices.schemas import invoice_schema, invoices_schema
from werkzeug.exceptions import NotFound, BadRequest
from typing import Dict, Any

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class InvoiceService:
    @staticmethod
    def get_invoice(invoice_id: str):
        invoice = InvoiceRepository.get_by_id(invoice_id)
        if not invoice:
            raise NotFound("Invoice not found")
        return invoice_schema.dump(invoice)

    @staticmethod
    def get_all_invoices():
        invoices = InvoiceRepository.get_all()
        return invoices_schema.dump(invoices)

    @staticmethod
    def create_invoice(data: dict):
        invoice = invoice_schema.load(data)
        InvoiceRepository.create(invoice)
        return invoice_schema.dump(invoice)

    @staticmethod
    def delete_invoice(invoice_id: str):
        invoice = InvoiceRepository.get_by_id(invoice_id)
        if not invoice:
            raise NotFound("Invoice not found")
        InvoiceRepository.delete(invoice)
        return '', 204
    
    @staticmethod
    def get_all_work_orders_paginated(page: int = 1, per_page: int = 10) -> Dict[str, Any]:
        """Get paginated work orders with metadata"""
        try:
            return InvoiceRepository.get_all_paginated(page=page, per_page=per_page)
        except Exception as e:
            logger.error(f"Error fetching paginated work orders: {e}")
            raise
