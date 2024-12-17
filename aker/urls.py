from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Configurator"
admin.site.index_title = "Configurator"
admin.site.site_title = "Lutia"

urlpatterns = [
    path("organizations/", include("organization.urls", namespace="organization")),
    path("configurator/", admin.site.urls),
]
