from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet

media_router = DefaultRouter()
media_router.register(r"medias", MediaViewSet)