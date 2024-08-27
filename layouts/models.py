from django.db import models
from medias.models import Media

# Create your models here.
class Layout(models.Model):
    card_desc = models.TextField(null=False)
    img_url = models.ForeignKey(Media, on_delete= models.SET_NULL, null=True)
    link = models.TextField(null=False)


    def __str__(self):
        return f"card: {self.card_desc}, comment: {self.img_url}, comment: {self.link}"