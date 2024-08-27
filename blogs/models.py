from django.db import models
from medias.models import Media

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100, null=False)
    text = models.TextField(null=False)
    img_url = models.ForeignKey(Media, on_delete= models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)