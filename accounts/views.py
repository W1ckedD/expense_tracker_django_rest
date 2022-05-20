from rest_framework import generics, permissions, response
from .serializers import AccountSerializer

class UserAccountView(generics.GenericAPIView):
  serializer_class = AccountSerializer
  permission_classes = [
    permissions.IsAuthenticated,
  ]

  def post(self, request):
    if request.user.account:
      return response.Response({
        'detail': 'Account already exists.'
      }, status=400)
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    account = serializer.save(user=request.user)

    return response.Response({
      'account': account.data
    })

  def get(self, request):
    account = self.get_serializer(request.user.account)
    return response.Response({
      'account': account.data
    })

  def put(self, request):
    serializer = self.get_serializer(request.user.account, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user)
    return response.Response({
      'account': self.get_serializer(request.user.account).data
    })