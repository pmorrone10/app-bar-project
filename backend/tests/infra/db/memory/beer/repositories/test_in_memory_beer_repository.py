from unittest import TestCase
from unittest.mock import MagicMock

from app.domain.entities.beer import Beer
from app.infra.db.memory.beer.adapter.beer_adapter import BeerAdapter
from app.infra.db.memory.beer.model.beer import BeerDto
from app.infra.db.memory.beer.repositories.in_memory_beer_repository import InMemoryBeerRepository


def get_data():
    return {
        'Quilmes': BeerDto(name='Quilmes', price=150.00, quantity=2)
    }


def get_expected_beer():
    return {'Quilmes': Beer(name='Quilmes', price=150.00, quantity=2)}


class TestInMemoryBeerRepository(TestCase):

    def setUp(self):
        self.adapter = MagicMock(spec=BeerAdapter)
        self.data = get_data()
        self.repository = InMemoryBeerRepository(self.data, self.adapter)

    def test_when_beer_data_is_empty(self):
        result = self.repository.get_beers_with_name(['Corona'])
        self.assertEqual({}, result)

    def test_when_beer_is_not_empty(self):
        self.adapter.transform.return_value = Beer(name='Quilmes', price=150.00, quantity=2)
        result = self.repository.get_beers_with_name(['Quilmes'])
        self.adapter.transform.assert_called_once_with(self.data['Quilmes'])
        self.assertEqual(get_expected_beer(), result)
