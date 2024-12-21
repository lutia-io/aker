from django_filters import rest_framework as filters
from user.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            "id": ["iexact", "icontains", "istartswith", "iendswith"],
            "uuid": ["iexact", "icontains", "istartswith", "iendswith"],
            "username": ["iexact", "icontains", "istartswith", "iendswith"],
            "first_name": ["iexact", "icontains", "istartswith", "iendswith"],
            "last_name": ["iexact", "icontains", "istartswith", "iendswith"],
            "email": ["iexact", "icontains", "istartswith", "iendswith"],
            "is_active": ["exact"],
            "date_joined": ["exact", "gt", "lt", "gte", "lte", "isnull"],
        }
