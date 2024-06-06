from config.errors import DomainException


class OutOfStock(DomainException):
    ...


class InsufficientStock(DomainException):
    ...
