from rest_framework.viewsets import ModelViewSet
from ..models import Layout
from .serializer import LayoutSerializer

class LayoutViewSet(ModelViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer