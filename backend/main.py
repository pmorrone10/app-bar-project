import locale

from fastapi import FastAPI

from app.api.fastapi.presenter.order_presenter import OrderPresenter
from app.api.fastapi.router.order_router import OrderRouter
from app.core.usecases.order_usecase import OrderUseCase

from app.infra.db.memory.beer.adapter.beer_adapter import BeerAdapter
from app.infra.db.memory.beer.model.beer import BeerDto
from app.infra.db.memory.beer.repositories.in_memory_beer_repository import InMemoryBeerRepository
from app.infra.db.memory.order.adapter.order_adapter import OrderAdapter
from app.infra.db.memory.order.model.order import OrderDto, OrderRoundDto, RoundItemDto
from app.infra.db.memory.order.repositories.in_memory_order_repository import InMemoryOrderRepository


def get_order_data():
    return {
        '1': OrderDto(order_id='1', created='2024-09-10 12:00:30', rounds=[OrderRoundDto(created='2024-09-10 12:00:30', items=[
            RoundItemDto(name='Corona', quantity=2), RoundItemDto(name='Club Colombia', quantity=1),
        ]),
                                                                  OrderRoundDto(
                                                                      created='2024-09-10 12:20:31',
                                                                      items=[
                                                                          RoundItemDto(name='Quilmes', quantity=1),
                                                                          RoundItemDto(name='Club Colombia',
                                                                                       quantity=2),
                                                                      ]),
                                                                  ],
                      ),
    }


def get_beer_data():
    return {
        'Quilmes': BeerDto(name='Quilmes', price=150.00, quantity=2),
        'Club Colombia': BeerDto(name='Club Colombia', price=200.00, quantity=3),
        'Corona': BeerDto(name='Corona', price=300.00, quantity=3),
    }


locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

app = FastAPI()

order_repository = InMemoryOrderRepository(data=get_order_data(), adapter=OrderAdapter())
beer_repository = InMemoryBeerRepository(data=get_beer_data(), adapter=BeerAdapter())

order_use_case = OrderUseCase(order_repository=order_repository, beer_repository=beer_repository, taxes=0.1)
order_presenter = OrderPresenter()
order_router = OrderRouter(usecase=order_use_case, presenter=order_presenter)
app.include_router(order_router.router, prefix="/api/v1", tags=["orders"])
