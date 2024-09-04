from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet, upload_image
from django.urls import path

media_router = DefaultRouter()
media_router.register(r"medias", MediaViewSet)

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
]
