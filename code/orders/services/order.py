from tinyinject import di
from orders.models import Order
from orders.models import Product
from orders.models import Stock
from orders.models import StockManager
from .product import reserve_stock
from .product import reconcilliate_stock

from .protocols import PlaceOrder


def send_wms_order(email, order):
    # placeholder
    return {
        'success': True,
    }


def send_crm_event(message, obj):
    # placeholder
    return


def send_mail(recipient, message):
    # placeholder
    return


@di.implements(interface=PlaceOrder)
def place_order(user, product: Product, quantity: int):
    order = Order.objects.create(
        user=user,
        product=product,
        quantity=quantity,
    )

    wms_order = send_wms_order(user.email, order)

    if not wms_order['success']:
        product.reconcilliate()

        send_crm_event('order_failed', order)
        return None

    product.reserve(quantity)

    send_mail(user.email, 'Your order was placed')
    send_crm_event('order_created', order)

    return order

