from user.models import User
from user.serializers import UserSerializer
from rest_framework import viewsets
from user.filters import UserFilter
from user.policy import UserPolicy
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = [UserPolicy]
    filterset_class = UserFilter
    ordering = ["-pk"]
    search_fields = ["id", "uuid", "username", "first_name", "last_name", "email"]
    ordering_fields = [
        "id",
        "uuid",
        "username",
        "first_name",
        "last_name",
        "email",
        "date_joined",
    ]
    http_method_names = ["get"]
    lookup_field = "uuid"

    @action(
        methods=["get"],
        detail=True,
        serializer_class=UserSerializer,
        queryset=User.objects.filter(),
        name="Me",
    )
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
