from typing import Protocols


class SendOrder(Protocol):
    def __call__(self, email: str, oid: int, quantity: int, ean: str):
        ...


class QueryStock(Protocol):
    def __call__(self, ean: str): 
        ...

