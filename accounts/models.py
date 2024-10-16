from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=False)
    USERNAME_FIELD="username"
    
    def __str__(self):
        return f"username: {self.username}"