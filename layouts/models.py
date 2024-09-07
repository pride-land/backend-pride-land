from django.db import models
from medias.models import Media

# Create your models here.
class Layout(models.Model):
    card_title = models.CharField(max_length=100, null=False, default='title')
    card_desc = models.TextField(null=False)
    img_url = models.ForeignKey(Media, on_delete= models.SET_NULL, null=True)
    link = models.TextField(null=False)
    
    def __str__(self):
        return f"Blog Name: {self.card_desc}, {self.link} "
