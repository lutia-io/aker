from django.contrib import admin
from record.models import Record
from record.forms import RecordChangeForm


class RecordAdmin(admin.ModelAdmin):
    form = RecordChangeForm
    list_display = (
        "id",
        "uuid",
        "schema",
        "user",
        "organization",
        "created_at",
        "updated_at",
    )
    search_fields = ("uuid", "schema", "user", "organization")
    list_filter = ("created_at", "updated_at", "schema", "organization")
    raw_id_fields = ("schema", "user", "organization")


admin.site.register(Record, RecordAdmin)
