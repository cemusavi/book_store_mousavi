from rest_framework.serializers import ModelSerializer
from address import models


class AddressSerializer(ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
            'city',
            'exact_address'
        )