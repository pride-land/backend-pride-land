from django.db import models
from medias.models import Media

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    content = models.TextField(null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Blog Name: {self.title}, {self.description}, {self.content} "

