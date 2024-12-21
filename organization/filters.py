from django_filters import rest_framework as filters
from organization.models import Organization


class OrganizationFilter(filters.FilterSet):
    class Meta:
        model = Organization
        fields = ["uuid", "created_at", "updated_at", "name", "slug"]
