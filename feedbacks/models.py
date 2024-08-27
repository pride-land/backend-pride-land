from django.db import models

# Create your models here.
class Feedback(models.Model):

    name = models.CharField(max_length=200, null=False)
    comment = models.TextField(null=False)

    def __str__(self):
        return f"name: {self.name}, comment: {self.comment}"