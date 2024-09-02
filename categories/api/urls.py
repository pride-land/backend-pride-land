from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet

categories_router = DefaultRouter()
categories_router.register(r"categories", CategoriesViewSet)