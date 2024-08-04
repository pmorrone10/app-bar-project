from app.domain.entities.order import Order, OrderRound, RoundItem
from app.infra.db.memory.order.model.order import OrderDto, OrderRoundDto, RoundItemDto


class OrderAdapter:

    def transform(self, order_dto: OrderDto) -> Order:
        rounds = list(map(lambda i: self.transform_round(i), order_dto.rounds))
        return Order(id=order_dto.order_id, created=order_dto.created, rounds=rounds)

    def transform_round(self, rounds_dto: OrderRoundDto):
        items = list(map(lambda i: self.transform_item(i), rounds_dto.items))
        return OrderRound(created=rounds_dto.created, items=items)

    def transform_item(self, items_dto: RoundItemDto) -> RoundItem:
        return RoundItem(name=items_dto.name, quantity=items_dto.quantity)
