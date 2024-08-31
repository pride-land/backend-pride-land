from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('core.api.urls')),
    path('api-reg/', include('accounts.api.urls')),
    path('api-pl/', include('pland_auth.api.urls')),
]
