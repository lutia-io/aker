from django.contrib import admin
from field.models import Field, FieldOption


class FieldOptionInline(admin.TabularInline):
    model = FieldOption

    extra = 1


class FieldAdmin(admin.ModelAdmin):
    list_display = ("name", "label", "schema", "user", "organization")
    list_filter = ("organization", "schema")
    search_fields = ("name", "label", "user__email", "organization__name")
    ordering = ("name",)
    inlines = [FieldOptionInline]


admin.site.register(Field, FieldAdmin)
