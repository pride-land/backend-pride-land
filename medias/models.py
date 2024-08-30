from django.db import models

# Create your models here.
class Media(models.Model):
    img_url = models.ImageField(default="default.jpg", upload_to="image_url")

    def __str__(self):
        return f"URL: {self.img_url}"