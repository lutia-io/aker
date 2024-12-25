from core.policy import BaseAccessPolicy


class RecordPolicy(BaseAccessPolicy):
    slug = "record-policy"

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs
