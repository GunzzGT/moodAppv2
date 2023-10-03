from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        try:
            CustomUser.objects.get(email=value)
            raise serializers.ValidationError("This email is already in use.")
        except CustomUser.MultipleObjectsReturned:
            raise serializers.ValidationError("Multiple users found with this email.")
        except CustomUser.DoesNotExist:
            return value.lower()

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("The password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("The password must contain at least one digit.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("The password must contain at least one lowercase letter.")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("The password must contain at least one uppercase letter.")
        return value

    def validate_nickname(self, value):
        OFFENSIVE_WORDS = ["shit", "fuck", ]
        lowercase_value = value.lower()
        for word in OFFENSIVE_WORDS:
            if word in lowercase_value:
                raise serializers.ValidationError("Nickname cannot contain inappropriate words")
        return value

    class Meta:
        model = CustomUser
        fields = ['user_id', 'email', 'password', 'name', 'nickname', 'telephone', 'address', 'gender', 'date_birth',
                  'role', 'created_at', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        profile = {
            'name': representation['name'],
            'nickname': representation['nickname'],
            'telephone': representation['telephone'],
            'address': representation['address'],
            'gender': representation['gender'],
            'date_birth': representation['date_birth'],

            'role': representation['role'],
            'created_at': representation['created_at'],
            'last_login': representation['last_login'],
        }
        response_data = {
            'user_id': representation['user_id'],
            'email': representation['email'],
            'profile': profile,
        }
        return response_data
