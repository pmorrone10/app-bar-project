from unittest import TestCase

from app.domain.entities.beer import Beer
from app.infra.db.memory.beer.adapter.beer_adapter import BeerAdapter
from app.infra.db.memory.beer.model.beer import BeerDto


class TestBeerAdapter(TestCase):

    def setUp(self):
        self.adapter = BeerAdapter()

    def test_transform_success(self):
        result = self.adapter.transform(BeerDto(name='Quilmes', price=150.0, quantity=2))
        self.assertEqual(Beer(name='Quilmes', price=150, quantity=2), result)
