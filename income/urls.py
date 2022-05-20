from django.urls import path
from . import views

urlpatterns = [
  path('', views.IncomeList.as_view(), name='income_income-list'),
  path('<int:id>/', views.IncomeListItem.as_view(), name='income_income-list-item'),
]