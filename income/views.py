from rest_framework import generics, permissions, response
from .serializers import IncomeSerializer
from .models import Income
from accounts.serializers import AccountSerializer
from utils.calculations import calculate_current_balance

class IncomeList(generics.ListCreateAPIView):
  serializer_class = IncomeSerializer
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  def get_queryset(self):
    return Income.objects.filter(account=self.request.user.account)

  def perform_create(self, serializer):
    serializer.save(account=self.request.user.account)
    account_serializer = AccountSerializer(self.request.user.account)
    account_serializer = AccountSerializer(
      self.request.user.account,
      data={'current_balance': calculate_current_balance(request=self.request)},
      partial=True
    )
    account_serializer.is_valid(raise_exception=True)
    account_serializer.save()

class IncomeListItem(generics.RetrieveUpdateDestroyAPIView):
  lookup_field = 'id'
  serializer_class = IncomeSerializer
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  def get_queryset(self):
    return Income.objects.filter(account=self.request.user.account)

  def perform_update(self, serializer):
    serializer.save(account=self.request.user.account, partial=True)
    account_serializer = AccountSerializer(self.request.user.account)
    account_serializer = AccountSerializer(
      self.request.user.account,
      data={'current_balance': calculate_current_balance(request=self.request)},
      partial=True
    )
    account_serializer.is_valid(raise_exception=True)
    account_serializer.save()


  def perform_destroy(self, instance):
    super().perform_destroy(instance)
    account_serializer = AccountSerializer(self.request.user.account)
    account_serializer = AccountSerializer(
      self.request.user.account,
      data={'current_balance': calculate_current_balance(request=self.request)},
      partial=True
    )
    account_serializer.is_valid(raise_exception=True)
    account_serializer.save()
    
    

