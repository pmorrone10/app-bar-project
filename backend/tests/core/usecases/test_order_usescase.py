from unittest import TestCase
from unittest.mock import MagicMock

from app.core.usecases.order_usecase import OrderUseCase
from app.domain.entities.beer import Beer
from app.domain.entities.order import Order, OrderRound, RoundItem, Item
from app.domain.exceptions.invalid_beer_exception import InvalidBeerException
from app.domain.exceptions.not_found_exception import NotFoundException
from app.domain.repositories.beer_repository import BeerRepository
from app.domain.repositories.order_repository import OrderRepository


def default_order():
    return Order(
        id='1',
        created='2024-09-10 12:00:00',
        paid=False,
        subtotal=0,
        total=0,
        taxes=0,
        discounts=0,
        items=[],
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


def expected_order_for_success():
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


class TestOrderUseCase(TestCase):

    def setUp(self):
        self.order_repository = MagicMock(spec=OrderRepository)
        self.beer_repository = MagicMock(spec=BeerRepository)
        self.order_usecase = OrderUseCase(order_repository=self.order_repository, beer_repository=self.beer_repository,
                                          taxes=0.1)

    def test_order_not_found(self):
        self.order_repository.get_order_by_id.return_value = None
        with self.assertRaises(NotFoundException):
            self.order_usecase.get_order("123")

    def test_when_order_exist(self):
        self.order_repository.get_order_by_id.return_value = default_order()

        self.beer_repository.get_beers_with_name.return_value = {'Quilmes': Beer(name='Quilmes', quantity=5, price=150.0),
                                                           'Club Colombia': Beer(name='Club Colombia', quantity=5,
                                                                                 price=200.0),
                                                           'Corona': Beer(name='Corona', quantity=5, price=300.0)}

        order = self.order_usecase.get_order(order_id='1')

        self.assertEqual(expected_order_for_success(), order)

    def test_when_item_of_round_not_exist_in_beers(self):
        self.order_repository.get_order_by_id.return_value = default_order()
        self.beer_repository.get_beers_with_name.return_value = {'Otra': Beer(name='Quilmes', quantity=5, price=150.0),
                                                                 'Club Colombia': Beer(name='Club Colombia', quantity=5,
                                                                                       price=200.0),
                                                                 'Corona': Beer(name='Corona', quantity=5, price=300.0)}

        with self.assertRaises(InvalidBeerException):
            self.order_usecase.get_order('123')
