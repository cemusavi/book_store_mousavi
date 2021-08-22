from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from address import models
from . import serializers


class AddAddress(generics.CreateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = IsAuthenticated, DjangoModelPermissions

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
