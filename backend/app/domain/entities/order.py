from dataclasses import dataclass, fields, field
from typing import List


# from pydantic import BaseModel

@dataclass(frozen=True)
class RoundItem:
    name: str
    quantity: int


@dataclass(frozen=True)
class OrderRound:
    created: str
    items: List[RoundItem]


@dataclass(frozen=True)
class Item:
    name: str
    unit_price: float
    total: float


@dataclass(frozen=True)
class Order:
    id: str
    created: str
    rounds: List[OrderRound]
    items: List[Item] = field(init=True, default_factory=list)
    paid: bool = False
    subtotal: float = 0.0
    taxes: float = 0.0
    total: float = 0.0
    discounts: float = 0.0
