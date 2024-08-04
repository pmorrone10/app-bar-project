import locale
from unittest import TestCase

from app.api.fastapi.presenter.order_presenter import OrderPresenter
from app.api.fastapi.schema.order_schema import OrderSchema, ItemSchema
from app.domain.entities.order import Order, Item, OrderRound, RoundItem


def get_data():
    return Order(
        id='1',
        created='2024-09-10 12:00:00',
        paid=False,
        subtotal=1350.0,
        taxes=135.0,
        discounts=0.0,
        total=1485.0,
        items=[
            Item(name='Corona', unit_price=300.0, total=600.0),
            Item(name='Club Colombia', unit_price=200.0, total=600.0),
            Item(name='Quilmes', unit_price=150.0, total=150.0),
        ],
        rounds=[
            OrderRound(
                created='2024-09-10 12:00:30',
                items=[
                    RoundItem(name='Corona', quantity=2),
                    RoundItem(name='Club Colombia', quantity=1),
                ]
            ),
            OrderRound(
                created='2024-09-10 12:20:31',
                items=[
                    RoundItem(name='Quilmes', quantity=1),
                    RoundItem(name='Club Colombia', quantity=2),
                ]
            )
        ]
    )


def get_expected_data():
    return OrderSchema(
        id='1',
        created='2024-09-10 12:00:00',
        paid=False,
        subtotal='$ 1.350,00',
        taxes='$ 135,00',
        discounts='$ 0,00',
        total='$ 1.485,00',
        items=[
            ItemSchema(name='Corona', unit_price='$ 300,00', total='$ 600,00'),
            ItemSchema(name='Club Colombia', unit_price='$ 200,00', total='$ 600,00'),
            ItemSchema(name='Quilmes', unit_price='$ 150,00', total='$ 150,00'),
        ]
    )


class TestOrderPresenter(TestCase):

    def setUp(self):
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        self.order_presenter = OrderPresenter()

    def test_success_transform(self):
        result = self.order_presenter.transform(get_data())
        self.assertEqual(get_expected_data(), result)
