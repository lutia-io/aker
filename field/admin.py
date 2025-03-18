from django.contrib import admin
from field.models import Field, FieldOption


class FieldOptionInline(admin.TabularInline):
    model = FieldOption
    extra = 1


class FieldAdmin(admin.ModelAdmin):
    list_display = ("name", "label", "type", "schema", "user", "organization")
    list_filter = ("organization", "schema")
    search_fields = ("name", "label", "user", "organization")
    inlines = [FieldOptionInline]


admin.site.register(Field, FieldAdmin)
