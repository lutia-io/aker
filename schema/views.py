from rest_framework import viewsets
from schema.serializers import SchemaSerializer
from schema.models import Schema
from schema.policy import SchemaPolicy
from django_filters.rest_framework import DjangoFilterBackend
from schema.filters import SchemaFilter


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    permission_classes = [SchemaPolicy]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchemaFilter
    http_method_names = ["get"]
    lookup_field = "uuid"
    search_fields = ["uuid", "name", "slug"]
    ordering = ["-pk"]

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)
