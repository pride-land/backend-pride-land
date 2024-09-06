from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import MediaViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static


media_router = DefaultRouter()
media_router.register(r"medias", MediaViewSet)

# urlpatterns = [
#     path('api/', include(media_router.urls))
# ]