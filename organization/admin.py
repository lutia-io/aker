from django.contrib import admin
from organization.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at", "updated_at", "user")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug", "user")
    raw_id_fields = ("user",)
    list_filter = ("created_at", "updated_at")


admin.site.register(Organization, OrganizationAdmin)
