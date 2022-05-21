from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='auth_register'),
  path('get-user/', views.UserView.as_view(), name='auth_get-user'),
  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]