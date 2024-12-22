from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from record.models import Record
from record.serializers import RecordSerializer
from record.filters import RecordFilter
from record.policy import RecordPolicy


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecordFilter
    permission_classes = [RecordPolicy]
    http_method_names = ["get", "post", "patch"]
    ordering = ["-pk"]
    lookup_field = "uuid"

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user, organization=self.request.user.organization
        )
