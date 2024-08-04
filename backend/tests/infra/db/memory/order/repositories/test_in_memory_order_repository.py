from unittest import TestCase
from unittest.mock import MagicMock

from app.domain.entities.order import Order, OrderRound, RoundItem
from app.infra.db.memory.order.adapter.order_adapter import OrderAdapter
from app.infra.db.memory.order.model.order import OrderDto, OrderRoundDto, RoundItemDto
from app.infra.db.memory.order.repositories.in_memory_order_repository import InMemoryOrderRepository


def get_data():
    return {
        '1': OrderDto(order_id='1',
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
                      ),
    }


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


class TestInMemoryOrderRepository(TestCase):

    def setUp(self):
        self.data = get_data()
        self.adapter = MagicMock(spec=OrderAdapter)
        self.repository = InMemoryOrderRepository(self.data, self.adapter)

    def test_when_order_id_is_not_in_dict(self):
        result = self.repository.get_order_by_id('2')
        self.assertIsNone(result)
        self.adapter.transform.assert_not_called()

    def test_when_order_id_is_present_in_dict(self):
        self.adapter.transform.return_value = expected_order()
        result = self.repository.get_order_by_id('1')
        self.adapter.transform.assert_called_with(self.data['1'])
        self.assertEqual(expected_order(), result)
