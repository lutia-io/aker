from django.urls import path
from record.views import RecordViewSet


app_name = "record"

urlpatterns = [
    path(route="", view=RecordViewSet.as_view({"get": "list"}), name="list"),
    path(
        route="<uuid:uuid>/",
        view=RecordViewSet.as_view({"get": "retrieve"}),
        name="detail",
    ),
]
