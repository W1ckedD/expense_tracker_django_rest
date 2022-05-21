from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class RegisterView(CreateAPIView):
  serializer_class = RegisterSerializer


class UserView(RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]

  serializer_class = UserSerializer
  def get_object(self):
    return self.request.user
