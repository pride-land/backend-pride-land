from django.db import models
from medias.models import Media

# Create your models here.
class Hero(models.Model):
    img_url = models.ForeignKey(Media, on_delete= models.SET_NULL, null=True)
    site_desc = models.TextField(null=False)
    logo = models.TextField(null=False)