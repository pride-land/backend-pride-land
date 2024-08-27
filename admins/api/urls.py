from rest_framework.routers import DefaultRouter
from .views import AdminViewSet
from django.urls import path

admin_router = DefaultRouter()
admin_router.register(r"admins", AdminViewSet)