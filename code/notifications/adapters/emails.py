from tinyinject import di
from common.ports.email import SendMail
from logging import getLogger

logger = getLogger(__name__)


@di.implements(interface=SendMail)
def _send_mail_impl(email: str, message: str):
    logger.info(f"Send email to {email}, message: {message}")
    
