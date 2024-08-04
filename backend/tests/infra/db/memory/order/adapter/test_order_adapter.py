from unittest import TestCase

from app.domain.entities.order import Order, OrderRound, RoundItem
from app.infra.db.memory.order.adapter.order_adapter import OrderAdapter
from app.infra.db.memory.order.model.order import OrderDto, OrderRoundDto, RoundItemDto


def get_data():
    return OrderDto(order_id='1',
                    created='2014-07-25',
                    rounds=[OrderRoundDto(
                        created='2024-09-10 12:00:30',
                        items=[
                            RoundItemDto(name='Corona', quantity=2),
                            RoundItemDto(name='Club Colombia', quantity=1),
                        ]),
                        OrderRoundDto(
                            created='2024-09-10 12:20:31',
                            items=[
                                RoundItemDto(name='Quilmes', quantity=1),
                                RoundItemDto(name='Club Colombia', quantity=2),
                            ]),
                    ],
                    )


def expected_order():
    return Order(id='1',
                 created='2014-07-25',
                 rounds=[OrderRound(
                     created='2024-09-10 12:00:30',
                     items=[
                         RoundItem(name='Corona', quantity=2),
                         RoundItem(name='Club Colombia', quantity=1)
                     ]),
                     OrderRound(
                         created='2024-09-10 12:20:31',
                         items=[
                             RoundItem(name='Quilmes', quantity=1),
                             RoundItem(name='Club Colombia', quantity=2)
                         ]
                     )
                 ])


class TestOrderAdapter(TestCase):

    def setUp(self):
        self.adapter = OrderAdapter()

    def test_transform_success(self):
        result = self.adapter.transform(get_data())
        self.assertEqual(expected_order(), result)
