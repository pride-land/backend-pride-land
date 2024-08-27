from rest_framework.viewsets import ModelViewSet
from ..models import Hero
from .serializer import HeroSerializer

class HeroViewSet(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer