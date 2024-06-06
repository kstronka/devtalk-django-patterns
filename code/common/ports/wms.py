from typing import Protocol
from typing import TypedDict


class WMSResponse(TypedDict):
    success: bool


class SendOrder(Protocol):
    def __call__(self, email: str, oid: int, quantity: int, ean: str) -> WMSResponse:
        ...


class QueryStock(Protocol):
    def __call__(self, ean: str) -> int: 
        ...

