from orders.models import Order
from orders.models import Product
from orders.models import Stock
from orders.models import StockManager


def send_wms_order(email, order):
    # placeholder
    return {
        'success': True,
    }
    

def query_wms_stock(product, stock):
    # placeholder
    return stock.quantity


def notify_allocation_team(product, stock):
    # placeholder
    # send message that stocks are going low
    return


def send_crm_event(message, obj):
    # placeholder
    return


def send_mail(recipient, message):
    # placeholder
    return


def place_order(user, product: Product, quantity: int):
    order = Order.objects.create(
        user=user,
        product=product,
        quantity=quantity,
    )

    stock = Stock.objects.for_product(product)

    wms_order = send_wms_order(user.email, order)

    if not wms_order['success']:
        stock.quantity = query_wms_stock(product, stock)
        stock.save()

        notify_allocation_team(product, stock)
        send_crm_event('order_failed', order)
        return None

    stock.reserved_quantity += order.quantity
    stock.save()

    send_mail(user.email, 'Your order was placed')
    send_crm_event('order_created', order)

    return order

