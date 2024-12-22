from django.urls import path
from record.views import RecordViewSet

app_name = "record"

urlpatterns = [
    path(
        route="",
        view=RecordViewSet.as_view({"get": "list", "post": "create"}),
        name="list",
    ),
    path(
        route="<uuid:uuid>/",
        view=RecordViewSet.as_view({"get": "retrieve", "patch": "partial_update"}),
        name="detail",
    ),
]
