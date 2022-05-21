from django.urls import path
from . import views

urlpatterns = [
  path('user-account/', views.UserAccountView.as_view(), name='accounts_create-account'),
]