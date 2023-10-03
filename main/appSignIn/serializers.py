from appSignUp.models import CustomUser
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }


class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
