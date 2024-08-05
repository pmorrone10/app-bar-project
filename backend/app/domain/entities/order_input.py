from dataclasses import dataclass


@dataclass(frozen=True)
class OrderInput:
    order_id: str
