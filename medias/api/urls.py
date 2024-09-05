from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static

media_router = DefaultRouter()
media_router.register(r"medias", MediaViewSet)

# urlpatterns = [
#     path('upload/', views.upload_image)
# ]

# from django.urls import path
# from .views import upload_base64

# urlpatterns = [
#     path('upload/', upload_base64, name='upload_base64'),
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)