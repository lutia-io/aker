from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, user):
        return user.get_full_name()

    class Meta:
        model = User
        fields = [
            "uuid",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "last_login",
            "is_active",
            "has_usable_password",
            "full_name",
        ]
