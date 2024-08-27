from rest_framework import ModelSerializer
from ..models import Volunteer

class VolunteerSerializer:
    class Meta:
        model = Volunteer
        fields = ("id", "name", "email", "start_date", "signup_date", "category", "restrictions", "status" )