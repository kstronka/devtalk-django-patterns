from tinyinject import di
from common.ports.crm import SendCrmEvent
from common.ports.email import SendMail
from common.ports.wms import SendOrder
from orders.models import Order
from orders.models import Product
from orders.models import Stock
from orders.models import StockManager

from .protocols import PlaceOrder


@di.implements(interface=PlaceOrder)
@di.require_kwargs(
    send_mail=SendMail,
    send_wms_order=SendOrder,
    send_crm_event=SendCrmEvent,
)
def place_order(
    user, 
    product: Product, 
    quantity: int,
    *,
    send_mail: SendMail,
    send_wms_order: SendOrder,
    send_crm_event: SendCrmEvent,
):
    order = Order.objects.create(
        user=user,
        product=product,
        quantity=quantity,
    )

    wms_order = send_wms_order(
        user.email, order.id, quantity, product.ean
    )

    if not wms_order['success']:
        product.reconcilliate()

        send_crm_event('order_failed', order)
        order.quantity = 0
        order.save()
        return order

    product.reserve(quantity)

    send_mail(user.email, 'Your order was placed')
    send_crm_event('order_created', order)

    return order

