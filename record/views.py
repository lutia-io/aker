from rest_framework import viewsets
from record.serializers import RecordSerializer
from record.models import Record
from record.policy import RecordPolicy


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by("-id")
    serializer_class = RecordSerializer
    permission_classes = [RecordPolicy]
    http_method_names = ["get"]
    lookup_field = "uuid"
    search_fields = ["uuid", "name", "slug", "active"]

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)
