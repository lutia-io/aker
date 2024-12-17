from django.urls import path
from organization.views import OrganizationViewSet


app_name = "organization"

urlpatterns = [
    path(route="", view=OrganizationViewSet.as_view({"get": "list"}), name="list"),
    path(route="<uuid:uuid>/", view=OrganizationViewSet.as_view({"get": "retrieve"}), name="detail"),
]
