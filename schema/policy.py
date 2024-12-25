from core.policy import BaseAccessPolicy


class SchemaPolicy(BaseAccessPolicy):
    slug = "schema-policy"

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs
