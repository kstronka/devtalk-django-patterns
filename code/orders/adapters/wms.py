from tinyinject import di
from common.ports.wms import SendOrder
from common.ports.wms import QueryStock
from common.ports.wms import WMSResponse
from logging import getLogger

logger = getLogger(__name__)


@di.implements(interface=SendOrder)
def _send_order_impl(email: str, oid: int, quantity: int, ean: str) -> WMSResponse:
    logger.info(f'POST WMS: {email=}, {oid=}, {quantity=}, {ean=}')
    return {'success': True}


@di.implements(interface=QueryStock)
def _query_stock_impl(ean: str) -> int:
    logger.info(f'QUERY WMS: {ean=}')
    return 100  # JIT delivery rocks

