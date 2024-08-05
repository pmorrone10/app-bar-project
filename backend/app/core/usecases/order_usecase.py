import dataclasses
from typing import Dict, List

from app.domain.entities.order import Order, Item
from app.domain.entities.order_input import OrderInput
from app.domain.exceptions.invalid_beer_exception import InvalidBeerException
from app.domain.exceptions.not_found_exception import NotFoundException
from app.domain.repositories.beer_repository import BeerRepository
from app.domain.repositories.order_repository import OrderRepository


class OrderUseCase:

    def __init__(self, order_repository: OrderRepository, beer_repository: BeerRepository, taxes: float):
        self.__repository = order_repository
        self.__beer_repository = beer_repository
        self.__taxes_percentage = taxes

    def get_order(self, orderInput: OrderInput) -> Order:
        order = self.__repository.get_order_by_id(orderInput.order_id)
        if order is None:
            raise NotFoundException()

        beers_in_rounds: Dict[str, int] = {}
        for r in order.rounds:
            for item in r.items:
                quantity = 0
                if item.name in beers_in_rounds:
                    quantity = beers_in_rounds[item.name]
                beers_in_rounds[item.name] = quantity + item.quantity

        items = self.__get_items(beers_in_rounds)
        order = dataclasses.replace(order, items=items)
        return self.__process_order(order)

    def __get_items(self, beer_dict: Dict[str, int]) -> List[Item]:
        beers = self.__beer_repository.get_beers_with_name(beer_dict.keys())
        items: List[Item] = []
        for name in beer_dict:
            if name not in beers:
                raise InvalidBeerException()
            quantity = beer_dict[name]
            unit_price = beers[name].price
            item = Item(name=name, unit_price=unit_price, total=unit_price * quantity)
            items.append(item)

        return items

    def __process_order(self, order: Order) -> Order:
        subtotal = sum(map(lambda item: item.total, order.items))
        taxes = subtotal * self.__taxes_percentage
        total = subtotal + taxes - order.discounts  ##Esto debe ser un monto, no un porcentaje

        return dataclasses.replace(order, subtotal=subtotal, taxes=taxes, total=total)
