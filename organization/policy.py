from core.policy import BaseAccessPolicy


class OrganizationPolicy(BaseAccessPolicy):
    slug = "organization-policy"

    def is_owner(self, request, view, action):
        organization = view.get_object()
        return request.user == organization.user

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs.filter(user=request.user)
