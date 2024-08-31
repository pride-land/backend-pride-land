from ..models import Admin
from rest_framework.serializers import ModelSerializer

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = ('__all__')