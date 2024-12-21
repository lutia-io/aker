from django.contrib import admin
from policy.models import PolicyDefinition
from policy.forms import PolicyDefinitionChangeForm


class PolicyDefinitionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    form = PolicyDefinitionChangeForm


admin.site.register(PolicyDefinition, PolicyDefinitionAdmin)
