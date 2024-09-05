import base64
from django.db import models


# Create your models here.
class Media(models.Model):

    imageUrl = models.ImageField(default="default.jpg", upload_to="image_url")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    data = models.BinaryField(null=True)

    def __str__(self):
        return f"URL: {self.imageUrl}"

# class Data(models.Model):

#     _data = models.TextField(
#             db_column='data',
#             blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    # data = property(get_data, set_data)
