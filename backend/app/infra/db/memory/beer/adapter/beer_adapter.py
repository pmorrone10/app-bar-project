from app.domain.entities.beer import Beer
from app.infra.db.memory.beer.model.beer import BeerDto


class BeerAdapter:

    def transform(self, beer: BeerDto) -> Beer:
        return Beer(
            name=beer.name,
            price=beer.price,
            quantity=beer.quantity
        )
