from django_filters import rest_framework as filters
from field.models import Field


class FieldFilter(filters.FilterSet):
    class Meta:
        model = Field
        fields = [
            "uuid",
            "created_at",
            "updated_at",
            "name",
            "label",
            "type",
            "schema",
            "user",
        ]
