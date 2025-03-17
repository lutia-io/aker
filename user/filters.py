from django_filters import rest_framework as filters
from user.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "date_joined",
        ]
