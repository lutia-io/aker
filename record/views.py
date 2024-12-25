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
    http_method_names = ["get"]
    ordering = ["-pk"]
    lookup_field = "uuid"
    
    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)
