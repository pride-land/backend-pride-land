from ..models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('__all__')

class UserRegistrationSerializer(serializers.ModelSerializer):  
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta: 
        model = CustomUser
        fields = ("id", "username", "password1", "password2")
        extra_kwargs = {"password": {"write_only": True}}
    
    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Password do not match!")
        
        password = attrs.get("password1", "")
        if len(password) < 8:
            raise serializers.ValidationError("Passwords must be at least 8 characters")
        
        return attrs
    
    def create(self, validate_data):
            password = validate_data.pop("password1")
            validate_data.pop("password2")

            return CustomUser.objects.create_user(password=password, **validate_data)
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials!")   