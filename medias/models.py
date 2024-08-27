from django.db import models

# Create your models here.
class Media(models.Model):
    img_url = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"URL: {self.img_url}"