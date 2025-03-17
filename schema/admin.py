from django.contrib import admin
from schema.models import Schema
from field.models import Field


class FieldInline(admin.TabularInline):
    model = Field
    extra = 1
    autocomplete_fields = ["user", "organization"]
    show_change_link = True
    can_delete = False


class SchemaAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "active", "user", "organization")
    list_filter = ("active", "organization")
    search_fields = ("name", "slug", "user__email", "organization__name")
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [FieldInline]


admin.site.register(Schema, SchemaAdmin)
