from tinyinject import di
from orders.models import Product
from orders.models import Stock

from .protocols import ReserveStock
from .protocols import ReconcilliateStock

    
def notify_allocation_team(product, stock):
    # placeholder
    # send message that stocks are going low
    return


def query_wms_stock(product, stock):
    # placeholder
    return stock.quantity


@di.implements(interface=ReserveStock)
def reserve_stock(product: Product, quantity: int) -> Stock:
    stock: Stock = product.stock

    stock.reserved_quantity += quantity
    stock.save()

    return stock


@di.implements(interface=ReconcilliateStock)
def reconcilliate_stock(product: Product) -> Stock:
    stock.quantity = query_wms_stock(product, stock)
    stock.save()

    notify_allocation_team(product, stock)
    return stock

