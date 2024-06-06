from tinyinject import di
from orders.models import Product
from orders.models import Stock

from .protocols import ReserveStock
from .protocols import ReconcilliateStock
from .errors import InsufficientStock
from .errors import OutOfStock

    
def notify_allocation_team(product, stock):
    # placeholder
    # send message that stocks are going low
    return


def query_wms_stock(product, stock):
    # placeholder
    return stock.quantity


@di.implements(interface=ReserveStock)
def reserve_stock(product: Product, quantity: int) -> Stock:
    stock = _validate_stock_exists(product) or product.stock

    if (stock.quantity - stock.reserved_quantity) < quantity:
        raise InsufficientStock

    stock.reserved_quantity += quantity
    stock.save()

    return stock


@di.implements(interface=ReconcilliateStock)
def reconcilliate_stock(product: Product) -> Stock:
    stock = _validate_stock_exists(product) or product.stock

    stock.quantity = query_wms_stock(product, stock)
    stock.save()

    notify_allocation_team(product, stock)
    return stock


def _validate_stock_exists(product: Product):
    if not product.stock:
        raise OutOfStock
        
