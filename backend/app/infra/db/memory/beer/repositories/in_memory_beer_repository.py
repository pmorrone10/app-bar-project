from typing import Dict, List

from app.domain.entities.beer import Beer
from app.domain.repositories.beer_repository import BeerRepository
from app.infra.db.memory.beer.adapter.beer_adapter import BeerAdapter
from app.infra.db.memory.beer.model.beer import BeerDto


class InMemoryBeerRepository(BeerRepository):

    def __init__(self, data: Dict[str, BeerDto], adapter: BeerAdapter) -> None:
        self.__data = data
        self.__adapter = adapter

    def get_beers_with_name(self, names: List[str]) -> Dict[str, Beer]:
        beers = {}
        for name in names:
            if name in self.__data:
                beer_dto = self.__data[name]
                beer = self.__adapter.transform(beer_dto)
                beers[name] = beer

        return beers
