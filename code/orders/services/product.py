from tinyinject import di
from common.ports.email import SendMail
from common.ports.wms import QueryStock
from orders.models import Product
from orders.models import Stock

from .protocols import ReserveStock
from .protocols import ReconcilliateStock
from .errors import InsufficientStock
from .errors import OutOfStock

    
@di.require_kwargs(send_mail=SendMail)
def notify_allocation_team(product, stock, *, send_mail: SendMail):
    # placeholder
    # send message that stocks are going low
    return send_mail(
        'allocation@example.org', 
        f'{product} stocks are runing low at {stock.quantity - stock.reserved_quantity=}',
    )


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
@di.require_kwargs(query_wms_stock=QueryStock)
def reconcilliate_stock(product: Product, *, query_wms_stock: QueryStock) -> Stock:
    stock = _validate_stock_exists(product) or product.stock

    stock.quantity = query_wms_stock(product.ean)
    stock.save()

    notify_allocation_team(product, stock)
    return stock


def _validate_stock_exists(product: Product):
    if not product.stock:
        raise OutOfStock
        
