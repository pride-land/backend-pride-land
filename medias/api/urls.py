from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from .views import uploadImage, imageData, deleteImage, MediaViewSet
from django.conf import settings

media_router = DefaultRouter()
media_router.register(r"medias", MediaViewSet)

urlpatterns = [
    # path('medias/', include(media_router.urls)),
    path(r'upload-img/', uploadImage, name="upload_img"),

    path(r'get-img/', imageData, name="get_img"),
    path(r'delete-img/', deleteImage, name="delete_img"),
    path(r'get-img/', imageData, name="get_img")
]
