from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    img_url = models.CharField(max_length=255, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)