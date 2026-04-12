from app.blueprints.work_orders.repositories.repository import WorkOrderRepository
from app.blueprints.work_orders.model import WorkOrder, OrderStatus, PriorityStatus
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from app.extensions import db
from typing import Dict, Any, Optional, List
from marshmallow import ValidationError
from app.blueprints.work_orders.schemas import work_order_schema

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
            return WorkOrderRepository.get_all_paginated(page=page, per_page=per_page)
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
            # Validate and deserialize input data
            validated_data = work_order_schema.load(data)

            # Handle enum fields
            if 'current_status' in validated_data:
                validated_data['current_status'] = OrderStatus(validated_data['current_status'])
            if 'priority' in validated_data:
                validated_data['priority'] = PriorityStatus(validated_data['priority'])

            work_order = WorkOrder(**validated_data)
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
            # Validate and deserialize input data (partial update)
            validated_data = work_order_schema.load(data, partial=True)

            # Handle enum fields
            if 'current_status' in validated_data:
                validated_data['current_status'] = OrderStatus(validated_data['current_status'])
            if 'priority' in validated_data:
                validated_data['priority'] = PriorityStatus(validated_data['priority'])

            # Update work order attributes
            for key, value in validated_data.items():
                setattr(work_order, key, value)

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