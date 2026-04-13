from app.extensions import db
from app.blueprints.work_order_extras.repositories.repository import CancelledWorkOrderRepository 


class CancelledWorkOrderService:

    @staticmethod
    def get_all_cancelled_work_orders():
        return CancelledWorkOrderRepository.get_all()

    @staticmethod
    def get_cancelled_work_order(cancelled_work_order_id):
        return CancelledWorkOrderRepository.get_by_id(cancelled_work_order_id)

    @staticmethod
    def create_cancelled_work_order(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_cancelled_work_order(cancelled_work_order_id, data):
        cancelled_work_order = CancelledWorkOrderRepository.get_by_id(cancelled_work_order_id)

        if not cancelled_work_order:
            return None

        for key, value in data.items():
            setattr(cancelled_work_order, key, value)

        db.session.commit()
        return cancelled_work_order

    @staticmethod
    def delete_cancelled_work_order(cancelled_work_order_id):
        cancelled_work_order = CancelledWorkOrderRepository.get_by_id(cancelled_work_order_id)

        if not cancelled_work_order:
            return None

        db.session.delete(cancelled_work_order)
        db.session.commit()
        return cancelled_work_order
