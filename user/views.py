from user.models import User
from user.serializers import UserSerializer
from rest_framework import viewsets
from user.filters import UserFilter
from user.policy import UserPolicy
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [UserPolicy]
    filterset_class = UserFilter
    search_fields = ["uuid", "username", "first_name", "last_name", "email"]
    http_method_names = ["get"]
    lookup_field = "uuid"

    @action(methods=["get"], detail=True)
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
