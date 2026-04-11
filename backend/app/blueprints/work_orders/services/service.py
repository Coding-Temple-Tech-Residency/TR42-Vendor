from app.blueprints.work_orders.repositories.repository import WorkOrderRepository
from app.blueprints.work_orders.model import WorkOrder

class WorkOrderService:

    @staticmethod
    def get_all_work_orders():
        return WorkOrderRepository.get_all()

    @staticmethod
    def get_work_order(work_order_id):
        return WorkOrderRepository.get_by_id(work_order_id)

    @staticmethod
    def create_work_order(data):
        work_order = WorkOrder(**data)
        return WorkOrderRepository.create(work_order)

    @staticmethod
    def update_work_order(work_order, data):
        for key, value in data.items():
            setattr(work_order, key, value)
        WorkOrderRepository.update()
        return work_order

    @staticmethod
    def delete_work_order(work_order):
        WorkOrderRepository.delete(work_order)
        return True