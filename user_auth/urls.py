from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='auth_register'),
  path('login/', views.LoginView.as_view(), name='auth_login'),
  path('get-user/', views.UserView.as_view(), name='auth_get-user'),
]