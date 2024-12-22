from django.contrib import admin
from schema.models import Schema
from schema.forms import SchemaChangeForm


class SchemaAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "user", "organization", "created_at", "updated_at")
    search_fields = ("name", "slug", "user", "organization")
    list_filter = ("organization",)
    prepopulated_fields = {"slug": ("name",)}
    form = SchemaChangeForm


admin.site.register(Schema, SchemaAdmin)
