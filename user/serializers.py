from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    is_active = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    full_name = serializers.SerializerMethodField()

    def get_has_usable_password(self, user):
        return user.has_usable_password()

    def get_full_name(self, user):
        return user.get_full_name()

    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
            "date_joined",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "has_usable_password",
            "full_name",
        ]
