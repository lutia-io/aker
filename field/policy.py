from core.policy import BaseAccessPolicy


class FieldPolicy(BaseAccessPolicy):
    slug = "field-policy"

    def is_owner(self, request, view, action):
        field = view.get_object()
        return request.user == field.user

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs.filter(user=request.user)
