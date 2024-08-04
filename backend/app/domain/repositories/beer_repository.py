import abc
from typing import List, Dict

from app.domain.entities.beer import Beer


class BeerRepository(abc.ABC):

    @abc.abstractmethod
    def get_beers_with_name(self, names: List[str]) -> Dict[str, Beer]:
        pass
