from rest_framework import serializers

from orders.models import Product
from orders.models import Stock
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

    def create(self, validated_data):
        return Order.place(
            user=self.context['request'].user,
            **validated_data,
        )


