from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet

hero_router = DefaultRouter()
hero_router.register(r"heros", HeroViewSet)