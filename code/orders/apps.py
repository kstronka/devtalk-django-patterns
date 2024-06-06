from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "orders"

    def ready(self):
        from .services import order  # noqa
        from .services import product  # noqa
        from .adapters import wms  # noqa

