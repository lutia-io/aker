from rest_framework import viewsets
from organization.serializers import OrganizationSerializer
from organization.models import Organization
# from organization.policy import OrganizationPolicy


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [OrganizationPolicy]
    http_method_names = ["get"]
    lookup_field = "uuid"
