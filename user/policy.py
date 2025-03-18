from rest_access_policy import AccessPolicy


class UserPolicy(AccessPolicy):
    statements = [
        {
            "action": ["me"],
            "effect": "allow",
            "principal": ["admin", "staff", "authenticated"],
        }
    ]

    def is_owner(self, request, view, action):
        user = view.get_object()
        return request.user.id == user.id
