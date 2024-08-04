import locale
from typing import List

from app.api.fastapi.schema.order_schema import OrderSchema, ItemSchema
from app.domain.entities.order import Order, Item


class OrderPresenter:

    def transform(self, order: Order) -> OrderSchema:
        return OrderSchema(id=order.id, created=order.created, paid=order.paid,
                           total=self.__convert_to_money(order.total),
                           subtotal=self.__convert_to_money(order.subtotal),
                           taxes=self.__convert_to_money(order.taxes),
                           discounts=self.__convert_to_money(order.discounts),
                           items=self.__transform_items(order.items)
                           )

    def __convert_to_money(self, num: float) -> str:
        currency = locale.currency(num, grouping=True).replace(' Eu', '').replace(' €', '')
        return '$ {}'.format(currency)

    def __transform_items(self, items: List[Item]) -> List[ItemSchema]:
        return list(
            map(lambda i: ItemSchema(name=i.name, unit_price=self.__convert_to_money(i.unit_price),
                                     total=self.__convert_to_money(i.total)),
                items))
