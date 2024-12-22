from django.urls import path
from schema.views import SchemaViewSet


app_name = "schema"

urlpatterns = [
    path(route="", view=SchemaViewSet.as_view({"get": "list"}), name="list"),
    path(
        route="<uuid:uuid>/",
        view=SchemaViewSet.as_view({"get": "retrieve"}),
        name="detail",
    ),
]
