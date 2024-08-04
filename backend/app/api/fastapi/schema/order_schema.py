from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ItemSchema:
    name: str
    unit_price: str
    total: str


@dataclass(frozen=True)
class OrderSchema:
    id: str
    created: str
    items: List[ItemSchema]
    paid: bool
    subtotal: str
    taxes: str
    total: str
    discounts: str
