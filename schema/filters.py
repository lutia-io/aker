from django_filters import rest_framework as filters
from schema.models import Schema


class SchemaFilter(filters.FilterSet):
    class Meta:
        model = Schema
        fields = [
            "uuid",
            "created_at",
            "updated_at",
            "name",
            "slug",
            "active",
        ]
