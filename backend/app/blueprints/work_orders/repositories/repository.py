from app.blueprints.work_orders.model import WorkOrder, OrderStatus
from app.extensions import db
from sqlalchemy import desc
from typing import List, Optional


class WorkOrderRepository:

    @staticmethod
    def get_all() -> List[WorkOrder]:
        return WorkOrder.query.all()

    @staticmethod
    def get_all_paginated(page: int = 1, per_page: int = 10) -> dict:
        query = WorkOrder.query.order_by(desc(WorkOrder.created_at))
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            'work_orders': pagination.items,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': pagination.page,
            'per_page': pagination.per_page,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev,
            'next_page': pagination.next_num if pagination.has_next else None,
            'prev_page': pagination.prev_num if pagination.has_prev else None
        }

    @staticmethod
    def get_by_id(work_order_id: str) -> Optional[WorkOrder]:
        return WorkOrder.query.get(work_order_id)

    @staticmethod
    def get_vendor_work_orders_paginated(
        vendor_id: str,
        status: str = "all",
        page: int = 1,
        per_page: int = 10
    ) -> dict:
        """Get paginated work orders for a specific vendor, optionally filtered by status"""
        query = WorkOrder.query.filter_by(assigned_vendor=vendor_id)
        
        # Filter by status if not "all"
        if status != "all":
            try:
                status_enum = OrderStatus[status.upper()]
                query = query.filter_by(current_status=status_enum)
            except KeyError:
                # Invalid status, return empty results
                return {
                    'work_orders': [],
                    'total': 0,
                    'pages': 0,
                    'current_page': page,
                    'per_page': per_page,
                    'has_next': False,
                    'has_prev': False,
                    'next_page': None,
                    'prev_page': None,
                    'error': f"Invalid status. Valid options: all, {', '.join([s.value for s in OrderStatus])}"
                }
        
        query = query.order_by(desc(WorkOrder.created_at))
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            'work_orders': pagination.items,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': pagination.page,
            'per_page': pagination.per_page,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev,
            'next_page': pagination.next_num if pagination.has_next else None,
            'prev_page': pagination.prev_num if pagination.has_prev else None
        }

    @staticmethod
    def create(work_order: WorkOrder) -> WorkOrder:
        db.session.add(work_order)
        db.session.commit()
        return work_order

    @staticmethod
    def update(work_order: WorkOrder) -> WorkOrder:
        db.session.commit()
        return work_order

    @staticmethod
    def delete(work_order: WorkOrder) -> None:
        db.session.delete(work_order)
        db.session.commit()