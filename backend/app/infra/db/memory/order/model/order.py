from dataclasses import dataclass
from typing import List


@dataclass
class RoundItemDto:
    name: str
    quantity: int


@dataclass
class OrderRoundDto:
    created: str
    items: List[RoundItemDto]


@dataclass
class OrderDto:
    order_id: str
    created: str
    rounds: List[OrderRoundDto]
