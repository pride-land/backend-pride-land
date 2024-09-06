import base64
from django.db import models

# class Media(models.Model):
#     ...
    
#     blob_img = models.BinaryField(default=b"", null=True)

#     def save(self, *args, **kwargs):
#         if self.blob_img:
            
#             img_blob = self.blob_img
         
#             print(img_blob)
#     #         # binaryImg = "".join(["{:08b}".format(x) for x in decodedImg])
#     #         self.image_b64 = decodedImg
#     #         print(decodedImg)
#             super(Media, self).save(*args, **kwargs)

#     def __str__(self):
#         return f"URL: {self.image_b64}"
    
class Media(models.Model):
    blob_img = models.BinaryField(default=b"", null=True)

    def save(self, *args, **kwargs):
        
            
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return f"Media ID: {self.id}"