from rest_framework import generics, permissions, response

from purchase.models import Purchase, PurchaseItem
from .serializers import PurchaseSerializer, PurchaseItemSerializer
from accounts.serializers import AccountSerializer
from utils.calculations import calculate_current_balance, calculate_purchase_total_price

class ListCreatePurchaseView(generics.ListCreateAPIView):
  serializer_class = PurchaseSerializer
  permission_classes = [
    permissions.IsAuthenticated,
  ]

  def get_queryset(self):
    return Purchase.objects.filter(account=self.request.user.account)

  def perform_create(self, serializer):
    serializer.save(account=self.request.user.account)

class RetrieveUpdateDestroyPurchaseView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field = 'id'
  serializer_class = PurchaseSerializer
  permission_classes = [
    permissions.IsAuthenticated,
  ]

  def get_queryset(self):
    return Purchase.objects.filter(account=self.request.user.account)

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

class ListCreatePurchaseItemView(generics.ListCreateAPIView):
  serializer_class = PurchaseItemSerializer
  permission_classes = [
    permissions.IsAuthenticated,
  ]

  def get_queryset(self):
    purchase_id = int(self.request.GET.get('request_id'))
    purchase = Purchase.objects.get(id=purchase_id, account=self.request.user.account)
    return purchase.items.all()

  def perform_create(self, serializer):
    purchase_id = int(self.request.GET.get('purchase_id'))
    purchase = Purchase.objects.get(id=purchase_id, account=self.request.user.account)
    serializer.save(purchase=purchase)
    purchase_serializer = PurchaseSerializer(purchase, data={'total_price': calculate_purchase_total_price(purchase)}, partial=True)
    purchase_serializer.is_valid(raise_exception=True)
    purchase_serializer.save()
    account_serializer = AccountSerializer(self.request.user.account)
    account_serializer = AccountSerializer(
      self.request.user.account,
      data={'current_balance': calculate_current_balance(request=self.request)},
      partial=True
    )
    account_serializer.is_valid(raise_exception=True)
    account_serializer.save()

class RetrieveUpdateDestroyPurchaseItemView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field = 'id'
  serializer_class = PurchaseItemSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]

  def get_queryset(self):
    purchase_id = int(self.request.GET.get('request_id'))
    purchase = Purchase.objects.get(id=purchase_id, account=self.request.user.account)
    return purchase.items.all()

  def perform_update(self, serializer):
    purchase_id = int(self.request.GET.get('purchase_id'))
    purchase = Purchase.objects.get(id=purchase_id, account=self.request.user.account)
    serializer.save(purchase=purchase, partial=True)
    purchase_serializer = PurchaseSerializer(purchase, data={'total_price': calculate_purchase_total_price(purchase)}, partial=True)
    purchase_serializer.is_valid(raise_exception=True)
    purchase_serializer.save()
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
    purchase_id = int(self.request.GET.get('purchase_id'))
    purchase = Purchase.objects.get(id=purchase_id, account=self.request.user.account)
    purchase_serializer = PurchaseSerializer(purchase, data={'total_price': calculate_purchase_total_price(purchase)}, partial=True)
    purchase_serializer.is_valid(raise_exception=True)
    purchase_serializer.save()
    account_serializer = AccountSerializer(self.request.user.account)
    account_serializer = AccountSerializer(
      self.request.user.account,
      data={'current_balance': calculate_current_balance(request=self.request)},
      partial=True
    )
    account_serializer.is_valid(raise_exception=True)
    account_serializer.save()