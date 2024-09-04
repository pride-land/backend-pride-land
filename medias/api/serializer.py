from rest_framework import serializers
from ..models import Media
from drf_extra_fields.fields import Base64ImageField

class MediaSerializer(serializers.ModelSerializer):
    image=Base64ImageField() 
    class Meta:
        model = Media
        fields = '__all__'