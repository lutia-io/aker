from django.contrib import admin
from django.urls import path, include
from aker import settings

admin.site.site_header = "Configurator"
admin.site.index_title = "Configurator"
admin.site.site_title = settings.ADMIN_SITE_TITLE

urlpatterns = [
    path("auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("organizations/", include("organization.urls", namespace="organization")),
    path("users/", include("user.urls", namespace="user")),
    path("schemas/", include("schema.urls", namespace="schema")),
    path("configurator/", admin.site.urls),
]
