from django.db import models

# # Create your models here.
# class Media(models.Model):

#     imageUrl = models.ImageField(default="default.jpg", upload_to="upload")
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
   
#     def __str__(self):
#         return f"URL: {self.imageUrl}"
    
import base64


class Media(models.Model):
    ...
    imageUrl = models.ImageField(upload_to=None)
    image_b64 = models.TextField(max_length=None , default='')

    def save(self, *args, **kwargs):
        if self.imageUrl:
            print(self.imageUrl.url)
            img_file = self.imageUrl
            convImage = base64.b64encode(img_file.read())
         
            print(convImage.isascii())
            decodedImg = base64.decodebytes(convImage)
            binaryImg = "".join(["{:08b}".format(x) for x in decodedImg])
            self.image_b64 = binaryImg

            super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return f"URL: {self.image_b64}"
    