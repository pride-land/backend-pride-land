from rest_framework.serializers import ModelSerializer
from ..models import Volunteer

class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ("__all__")