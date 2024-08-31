from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VolunteerViewSet

volunteer_router = DefaultRouter()
volunteer_router.register("volunteers", VolunteerViewSet)