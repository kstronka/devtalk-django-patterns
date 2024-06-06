from tinyinject import di
from common.ports.crm import SendCrmEvent
from logging import getLogger

logger = getLogger(__name__)


@di.implements(interface=SendCrmEvent)
def _send_event_impl(message: str, obj):
    logger.info(f"Send CRM event {message} for {obj}")
    return

