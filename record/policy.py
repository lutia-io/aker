from core.policy import BaseAccessPolicy


class RecordPolicy(BaseAccessPolicy):
    slug = "record-policy"

    def is_owner(self, request, view, action):
        record = view.get_object()
        return request.user == record.user

    @classmethod
    def scope_queryset(cls, request, qs):
        return qs.filter(user=request.user)
