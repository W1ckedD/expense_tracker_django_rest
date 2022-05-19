from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from knox.views import AuthToken

class RegisterView(GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request):
    serializer = self.get_serializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    _, token = AuthToken.objects.create(user)

    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

class LoginView(GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)

    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

class UserView(RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]

  serializer_class = UserSerializer
  def get_object(self):
    return self.request.user
