from app.blueprints.invoices.repositories.invoice_repositories import LineItemRepository
from app.blueprints.invoices.model import LineItem
from app.blueprints.invoices.schemas import line_item_schema, line_items_schema
from werkzeug.exceptions import NotFound, BadRequest

class LineItemService:
    @staticmethod
    def get_line_item(line_item_id: str):
        line_item = LineItemRepository.get_by_id(line_item_id)
        if not line_item:
            raise NotFound("Line item not found")
        return line_item_schema.dump(line_item)

    @staticmethod
    def get_all_line_items():
        line_items = LineItemRepository.get_all()
        return line_items_schema.dump(line_items)

    @staticmethod
    def create_line_item(data: dict):
        line_item = line_item_schema.load(data)
        LineItemRepository.create(line_item)
        return line_item_schema.dump(line_item)

    @staticmethod
    def delete_line_item(line_item_id: str):
        line_item = LineItemRepository.get_by_id(line_item_id)
        if not line_item:
            raise NotFound("Line item not found")
        LineItemRepository.delete(line_item)
        return '', 204
