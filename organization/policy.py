from core.policy import BaseAccessPolicy


class OrganizationPolicy(BaseAccessPolicy):
    slug = "organization-policy"

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs
