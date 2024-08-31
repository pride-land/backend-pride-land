from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet

feedback_router = DefaultRouter()
feedback_router.register(r"feedbacks", FeedbackViewSet)