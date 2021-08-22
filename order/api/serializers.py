from rest_framework import serializers
from order import models


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderDetail
        fields = (
            'book',
            'order',
            'quantity'
        )
