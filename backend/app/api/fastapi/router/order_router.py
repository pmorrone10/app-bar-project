from fastapi import APIRouter, HTTPException

from app.api.fastapi.presenter.order_presenter import OrderPresenter
from app.api.fastapi.schema.order_schema import OrderSchema
from app.core.usecases.order_usecase import OrderUseCase
from app.domain.entities.order_input import OrderInput
from app.domain.exceptions.not_found_exception import NotFoundException
from app.domain.exceptions.invalid_beer_exception import InvalidBeerException


class OrderRouter:

    def __init__(self, usecase: OrderUseCase, presenter: OrderPresenter):
        self.router = APIRouter()
        self.__order_usecase = usecase
        self._setup_routes()
        self.__presenter = presenter

    def _setup_routes(self):
        @self.router.get("/order/{order_id}")
        def get_order_status(order_id: str):
            try:
                order = self.__order_usecase.get_order(orderInput=OrderInput(order_id))
                return self.__presenter.transform(order)
            except NotFoundException:
                raise HTTPException(status_code=404, detail="Order not found")
            except InvalidBeerException:
                raise HTTPException(status_code=500, detail='There is a problem loading beers')
            except Exception:
                raise HTTPException(status_code=500, detail="Internal Error")
