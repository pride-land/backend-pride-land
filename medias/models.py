import base64
from django.db import models

class Media(models.Model):
    blob_img = models.BinaryField(default=b"", null=True)

    def save(self, *args, **kwargs):
        
            
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return f"Media ID: {self.id}"