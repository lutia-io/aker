from django.urls import path
from field.views import FieldViewSet


app_name = "field"

urlpatterns = [
    path(route="", view=FieldViewSet.as_view({"get": "list"}), name="list"),
    path(
        route="<uuid:uuid>/",
        view=FieldViewSet.as_view({"get": "retrieve"}),
        name="detail",
    ),
]
