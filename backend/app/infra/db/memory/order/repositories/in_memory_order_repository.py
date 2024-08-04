from typing import Dict

from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository
from app.infra.db.memory.order.adapter.order_adapter import OrderAdapter
from app.infra.db.memory.order.model.order import OrderDto


class InMemoryOrderRepository(OrderRepository):

    def __init__(self, data: Dict[str, OrderDto], adapter: OrderAdapter):
        self.__data = data
        self.__adapter = adapter

    def get_order_by_id(self, order_id: str) -> Order:
        if order_id not in self.__data:
            return None

        order = self.__data[order_id]
        return self.__adapter.transform(order)
