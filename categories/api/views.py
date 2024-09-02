from rest_framework.viewsets import ModelViewSet
from ..models import Categories
from .serializers import CategoriesSerializer

class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer