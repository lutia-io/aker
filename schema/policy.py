from core.policy import BaseAccessPolicy


class SchemaPolicy(BaseAccessPolicy):
    slug = "schema-policy"

    def is_owner(self, request, view, action):
        schema = view.get_object()
        return request.user == schema.user

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs.filter(user=request.user)
