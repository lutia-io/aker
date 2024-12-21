from django.urls import path
from user.views import UserViewSet

app_name = "user"

urlpatterns = [
    path(route="", view=UserViewSet.as_view({"get": "list"}), name="list"),
    path(route="me/", view=UserViewSet.as_view({"get": "me"}), name="me"),
    path(
        route="<uuid:uuid>/",
        view=UserViewSet.as_view({"get": "retrieve"}),
        name="detail",
    ),
]
