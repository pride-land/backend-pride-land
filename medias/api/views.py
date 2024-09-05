from rest_framework.viewsets import ModelViewSet
from ..models import Media
from .serializer import MediaSerializer

#test imports
import base64
from io import BytesIO
from PIL import Image as PILImage
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Media

class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer



