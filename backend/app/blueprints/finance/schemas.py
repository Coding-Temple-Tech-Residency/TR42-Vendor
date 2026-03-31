from app.extensions import ma
from app.models.finance import LineItem


class LineItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LineItem
        load_instance = True


line_item_schema = LineItemSchema()
line_items_schema = LineItemSchema(many=True)