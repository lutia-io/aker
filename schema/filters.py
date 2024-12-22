from django_filters import rest_framework as filters
from schema.models import Schema


class SchemaFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    slug = filters.CharFilter(lookup_expr="iexact")
    user = filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    organization = filters.CharFilter(
        field_name="organization__name", lookup_expr="icontains"
    )

    class Meta:
        model = Schema
        fields = [
            "uuid",
            "created_at",
            "updated_at",
            "name",
            "slug",
            "user",
            "organization",
        ]
