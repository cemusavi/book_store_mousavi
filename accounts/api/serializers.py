from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    old_pass = serializers.CharField()
    new_pass = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'old_pass',
            'password',
            'new_pass',
        )

    def validate(self, attrs):
        data = self.initial_data
        password = data.get('new_password')
        re_pass = data.get('repeat_new_password')
        if password != re_pass:
            raise serializers.ValidationError(_('Passwords dont match!'))
        return data
