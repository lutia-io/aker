from core.policy import BaseAccessPolicy


class UserPolicy(BaseAccessPolicy):
    slug = "user-policy"

    def is_owner(self, request, view, action):
        user = view.get_object()
        return request.user.id == user.id
