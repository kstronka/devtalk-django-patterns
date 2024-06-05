from typing import Protocol
from typing import Union
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from orders.models import Order
    from orders.models import Product
    from orders.models import Stock
    from django.contrib.auth.models import User


class PlaceOrder(Protocol):
    def __call__(self, user: 'User', product: 'Product', quantity: int) -> Union['Order', None]:
        ...


class ReserveStock(Protocol):
    def __call__(self, product: 'Product', quantity: int) -> 'Stock':
        ...


class ReconcilliateStock(Protocol):
    def __call__(self, product: 'Product') -> 'Stock':
        ...

