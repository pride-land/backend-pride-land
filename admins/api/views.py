from ..models import Admin
from rest_framework.viewsets import ModelViewSet
from .serializers import AdminSerializer

class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer