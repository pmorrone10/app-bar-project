from unittest import TestCase
from unittest.mock import MagicMock

from fastapi import FastAPI
from starlette.testclient import TestClient

from app.api.fastapi.presenter.order_presenter import OrderPresenter
from app.api.fastapi.router.order_router import OrderRouter
from app.api.fastapi.schema.order_schema import OrderSchema, ItemSchema
from app.core.usecases.order_usecase import OrderUseCase
from app.domain.entities.order import Order
from app.domain.exceptions.invalid_beer_exception import InvalidBeerException
from app.domain.exceptions.not_found_exception import NotFoundException


def get_order_schema() -> OrderSchema:
    return OrderSchema(id='1', created='2024-09-10 12:00:00', paid=False,
                       subtotal='$ 1.350,00',
                       taxes='$ 135,00',
                       discounts='$ 0,00',
                       total='$ 1.485,00',
                       items=[
                           ItemSchema(name='Corona', unit_price='$ 300,00',
                                      total='$ 600,00'),
                           ItemSchema(name='Club Colombia', unit_price='$ 200,00',
                                      total='$ 600,00'),
                           ItemSchema(name='Quilmes', unit_price='$ 150,00',
                                      total='$ 150,00'),
                       ]
                       )


def get_expected_data() -> dict:
    return {
        "id": "1",
        "created": "2024-09-10 12:00:00",
        "items": [
            {
                "name": "Corona",
                "unit_price": "$ 300,00",
                "total": "$ 600,00"
            },
            {
                "name": "Club Colombia",
                "unit_price": "$ 200,00",
                "total": "$ 600,00"
            },
            {
                "name": "Quilmes",
                "unit_price": "$ 150,00",
                "total": "$ 150,00"
            }
        ],
        "paid": False,
        "subtotal": "$ 1.350,00",
        "taxes": "$ 135,00",
        "total": "$ 1.485,00",
        "discounts": "$ 0,00"
    }


class TestOrderRouter(TestCase):

    def setUp(self):
        self.app = FastAPI()
        self.client = TestClient(self.app)
        self.usecase = MagicMock(spec=OrderUseCase)
        self.presenter = MagicMock(spec=OrderPresenter)
        self.router = OrderRouter(self.usecase, self.presenter)
        self.app.include_router(self.router.router)

    def test_get_order_status_success(self):
        self.usecase.get_order.return_value = Order(id='', created='', rounds=[])
        self.presenter.transform.return_value = get_order_schema()
        response = self.client.get('/order/1')
        self.assertEqual(get_expected_data(), response.json())
        self.assertEqual(200, response.status_code)

    def test_get_order_status_not_found(self):
        self.usecase.get_order.side_effect = NotFoundException
        response = self.client.get('/order/1')
        self.assertEqual({'detail': 'Order not found'}, response.json())
        self.assertEqual(404, response.status_code)

    def test_get_order_invalid_beer_exception(self):
        self.usecase.get_order.side_effect = InvalidBeerException
        response = self.client.get('/order/1')
        self.assertEqual({'detail': 'There is a problem loading beers'}, response.json())
        self.assertEqual(500, response.status_code)

    def test_get_order_basic_exception(self):
        self.usecase.get_order.side_effect = Exception
        response = self.client.get('/order/1')
        self.assertEqual({'detail': 'Internal Error'}, response.json())
        self.assertEqual(500, response.status_code)
