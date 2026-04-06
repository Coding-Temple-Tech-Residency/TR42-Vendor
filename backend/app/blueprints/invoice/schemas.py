from app.extensions import ma
from invoice.model import Invoice


class InvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice
        load_instance = True


invoice_schema = InvoiceSchema()
invoices_schema = InvoiceSchema(many=True)