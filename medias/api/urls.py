from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import MediaViewSet
from . import views

media_router = DefaultRouter()
media_router.register(r"medias", MediaViewSet)

urlpatterns = [
    path('binary/', views.uploadImage)
]

from django.urls import path


urlpatterns = [
    path('get-data/', views.imageData),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)