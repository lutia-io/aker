from django.urls import path
from user.views import UserViewSet

app_name = "user"

urlpatterns = [
    path(route="me/", view=UserViewSet.as_view({"get": "me"}), name="me"),
]
