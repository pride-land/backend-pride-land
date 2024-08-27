from rest_framework.viewsets import ModelViewSet
from ..models import Media
from .serializer import MediaSerializer

class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer