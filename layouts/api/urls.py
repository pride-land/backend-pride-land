from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LayoutViewSet

layout_router = DefaultRouter()
layout_router.register(r"layouts", LayoutViewSet)