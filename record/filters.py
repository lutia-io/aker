from django_filters import rest_framework as filters
from record.models import Record


class RecordFilter(filters.FilterSet):
    schema = filters.CharFilter(field_name="schema__name", lookup_expr="icontains")
    user = filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    organization = filters.CharFilter(
        field_name="organization__name", lookup_expr="icontains"
    )
    created_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Record
        fields = ["schema", "user", "organization", "created_at", "updated_at"]
