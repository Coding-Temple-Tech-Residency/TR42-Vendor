from app.blueprints.work_orders.repositories.repository import WorkOrderRepository
from app.blueprints.work_orders.model import WorkOrder, OrderStatus, PriorityStatus
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from app.extensions import db
from typing import Dict, Any, Optional, List
from marshmallow import ValidationError
from app.blueprints.work_orders.schemas import work_order_schema, work_orders_schema

from app.blueprints.user.model import User
from app.blueprints.user.repositories.user_repositories import UserRepository
from app.blueprints.user.schemas import users_schema

from logging import getLogger


logger = getLogger(__name__)

class WorkOrderService:

    @staticmethod
    def get_all_work_orders() -> List[WorkOrder]:
        return WorkOrderRepository.get_all()

    @staticmethod
    def get_all_work_orders_paginated(page: int = 1, per_page: int = 10) -> Dict[str, Any]:
        """Get paginated work orders with metadata"""
        try:
            result = WorkOrderRepository.get_all_paginated(page=page, per_page=per_page)
            result["work_orders"] = work_orders_schema.dump(result.get("work_orders", []))
            return result
        except Exception as e:
            logger.error(f"Error fetching paginated work orders: {e}")
            raise

    @staticmethod
    def get_work_order(work_order_id: str) -> Optional[WorkOrder]:
        """Get a single work order by ID"""
        try:
            return WorkOrderRepository.get_by_id(work_order_id)
        except Exception as e:
            logger.error(f"Error fetching work order {work_order_id}: {e}")
            raise

    @staticmethod
    def create_work_order(data: Dict[str, Any]) -> WorkOrder:
        """Create a new work order from validated data"""
        try:
            # schema has load_instance=True so .load() returns a WorkOrder directly
            work_order = work_order_schema.load(data)
            return WorkOrderRepository.create(work_order)

        except ValidationError as e:
            logger.error(f"Validation error creating work order: {e.messages}")
            raise BadRequest(f"Invalid data: {e.messages}")
        except IntegrityError as e:
            logger.error(f"Database integrity error creating work order: {e}")
            db.session.rollback()
            raise BadRequest("Database constraint violation")
        except Exception as e:
            logger.error(f"Error creating work order: {e}")
            db.session.rollback()
            raise

    @staticmethod
    def update_work_order(work_order: WorkOrder, data: Dict[str, Any]) -> WorkOrder:
        """Update an existing work order with validated data"""
        try:
            assigned_vendor = data.get("assigned_vendor")
            if isinstance(assigned_vendor, str) and assigned_vendor.strip().startswith("{{") and assigned_vendor.strip().endswith("}}"):
                raise BadRequest(
                    "assigned_vendor contains an unresolved variable. Check your Postman environment variable name/value."
                )

            # schema has load_instance=True so passing instance= updates it in place
            work_order = work_order_schema.load(data, partial=True, instance=work_order)

            return WorkOrderRepository.update(work_order)

        except ValidationError as e:
            logger.error(f"Validation error updating work order: {e.messages}")
            raise BadRequest(f"Invalid data: {e.messages}")
        except IntegrityError as e:
            logger.error(f"Database integrity error updating work order: {e}")
            db.session.rollback()
            raise BadRequest("Database constraint violation")
        except Exception as e:
            logger.error(f"Error updating work order: {e}")
            db.session.rollback()
            raise

    @staticmethod
    def delete_work_order(work_order: WorkOrder) -> bool:
        """Delete a work order"""
        try:
            WorkOrderRepository.delete(work_order)
            return True
        except Exception as e:
            logger.error(f"Error deleting work order: {e}")
            db.session.rollback()
            raise

    @staticmethod
    def get_vendor_work_orders_paginated(vendor_id: str, status: str = "all", page: int = 1, per_page: int = 10) -> Dict[str, Any]:
        """Get paginated work orders for a vendor, optionally filtered by status"""
        try:
            result = WorkOrderRepository.get_vendor_work_orders_paginated(
                vendor_id=vendor_id,
                status=status,
                page=page,
                per_page=per_page
            )
            result["work_orders"] = work_orders_schema.dump(result.get("work_orders", []))
            return result
        except Exception as e:
            logger.error(f"Error fetching vendor work orders for {vendor_id} with status {status}: {e}")
            raise

    @staticmethod
    def _validate_status_assignment_rule(data: Dict[str, Any], existing: Optional[WorkOrder] = None) -> None:
        # Use incoming value, or fall back to existing value on partial updates
        status = data.get("current_status", existing.current_status if existing else None)
        assigned_vendor = data.get("assigned_vendor", existing.assigned_vendor if existing else None)

        # status may be enum after schema load; normalize to string value
        if hasattr(status, "value"):
            status_value = status.value
        else:
            status_value = status

        # Treat None/empty as unassigned
        is_unassigned = assigned_vendor in (None, "")

        # Rule 1: Pending requires Unassigned
        if status_value == "Pending" and not is_unassigned:
            raise BadRequest("Pending work orders must be unassigned")

        # Unassigned can only be Pending
        if is_unassigned and status_value != "Pending":
            raise BadRequest("Unassigned work orders must have status Pending")