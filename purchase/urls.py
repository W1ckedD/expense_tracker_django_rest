from django.urls import path
from . import views

urlpatterns = [
  path('', views.ListCreatePurchaseView.as_view(), name='purchase_purchase_list'),
  path('<int:id>/', views.RetrieveUpdateDestroyPurchaseView.as_view(), name='purchase_purchase'),
  path('items/', views.ListCreatePurchaseItemView.as_view(), name='purchase_purchase'),
]