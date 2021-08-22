from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers

User = get_user_model()


class ChangePassword(generics.UpdateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = IsAuthenticated,

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=user.username,
                password=serializer.validated_data['old_pass']
            )
            if user is not None:
                user.set_password(serializer.validated_data['new_pass'])
                user.save()
                return Response({'message': 'okay'}, status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
