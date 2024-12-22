from django.contrib import admin
from record.models import Record
from record.forms import RecordChangeForm


class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "schema",
        "user",
        "organization",
        "created_at",
        "updated_at",
    )
    search_fields = ("uuid", "schema__name", "user__username", "organization__name")
    list_filter = ("schema", "organization", "created_at")
    form = RecordChangeForm
    raw_id_fields = ("schema", "user", "organization")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("schema", "user", "organization")


admin.site.register(Record, RecordAdmin)