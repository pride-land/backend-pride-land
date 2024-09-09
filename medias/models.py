import base64
from django.db import models

class Media(models.Model):
    blob_img = models.BinaryField(default=b"", null=True)
    set_as_hero = models.BooleanField(default=False)
    alt_text = models.CharField(max_length=150, name=False, default='image')

    def save(self, *args, **kwargs):
        
            
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return f"Media ID: {self.id} {self.alt_text} {self.blob_img}"