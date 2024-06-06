from django.db import transaction
from config.errors import DomainException
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def create(self, *args, **kwargs):
        try:
            return super(OrderViewSet, self).create(*args, **kwargs)
        except DomainException as e:
            transaction.set_rollback(True)
            return Response(
                {'detail': str(e.code)},
                status=status.HTTP_400_BAD_REQUEST,
            )

