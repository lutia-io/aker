from rest_framework import viewsets
from organization.serializers import OrganizationSerializer
from organization.models import Organization
from organization.policy import OrganizationPolicy
from django_filters.rest_framework import DjangoFilterBackend
from organization.filters import OrganizationFilter


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [OrganizationPolicy]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganizationFilter
    http_method_names = ["get"]
    lookup_field = "uuid"
    search_fields = ["uuid", "name", "slug"]
    ordering = ["-pk"]
