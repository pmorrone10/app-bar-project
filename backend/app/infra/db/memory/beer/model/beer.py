from dataclasses import dataclass


@dataclass
class BeerDto:
    name: str
    price: float
    quantity: int
