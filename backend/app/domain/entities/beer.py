from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Beer:
    name: str
    price: float
    quantity: int
