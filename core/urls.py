from xml.etree.ElementInclude import include
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('income/', include('income.urls')),
    path('purchase/', include('purchase.urls')),
]
