from rest_framework import viewsets
from organization.serializers import OrganizationSerializer
from organization.models import Organization
from organization.policy import OrganizationPolicy
from organization.filters import OrganizationFilter


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [OrganizationPolicy]
    filterset_class = OrganizationFilter
    http_method_names = ["get"]
    lookup_field = "uuid"
    search_fields = ["uuid", "name", "slug"]

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)
