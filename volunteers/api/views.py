from rest_framework.viewsets import ModelViewSet
from serializers import VolunteerSerializer
from ..models import Volunteer

class VolunteerViewSet(ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
