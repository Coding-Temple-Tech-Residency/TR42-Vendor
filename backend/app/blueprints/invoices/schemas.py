from app.extensions import ma
from app.blueprints.invoices.model import Invoice, LineItem


class InvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice
        load_instance = True


invoice_schema = InvoiceSchema()
invoices_schema = InvoiceSchema(many=True)

class LineItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LineItem
        load_instance = True


line_item_schema = LineItemSchema()
line_items_schema = LineItemSchema(many=True)