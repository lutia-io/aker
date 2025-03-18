from rest_access_policy import AccessPolicy


class OrganizationPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "effect": "allow",
            "principal": ["admin", "staff", "authenticated"],
        }
    ]

    def is_owner(self, request, view, action):
        organization = view.get_object()
        return request.user == organization.user

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs.filter(user=request.user)
