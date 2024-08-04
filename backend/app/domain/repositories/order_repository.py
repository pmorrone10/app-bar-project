import abc

from app.domain.entities.order import Order


class OrderRepository(abc.ABC):

    @abc.abstractmethod
    def get_order_by_id(self, order_id: str) -> Order:
        pass
