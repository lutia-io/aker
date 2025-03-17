from rest_framework import viewsets
from field.serializers import FieldSerializer
from field.models import Field
from field.policy import FieldPolicy
from django_filters.rest_framework import DjangoFilterBackend
from field.filters import FieldFilter


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all().order_by("-id")
    serializer_class = FieldSerializer
    permission_classes = [FieldPolicy]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FieldFilter
    http_method_names = ["get"]
    lookup_field = "uuid"
    search_fields = ["uuid", "name", "label"]

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)
