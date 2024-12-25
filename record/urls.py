from django.urls import path
from record.views import RecordViewSet

app_name = "record"

urlpatterns = [
    path(
        route="<uuid:uuid>/",
        view=RecordViewSet.as_view({"get": "retrieve"}),
        name="detail",
    ),
    path(
        route="schema/<str:schema_name>/",
        view=RecordViewSet.as_view({"get": "list"}),
        name="list_by_schema",
    ),
]
