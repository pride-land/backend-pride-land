from django.db import models


# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(null=False)
    email = models.EmailField(null=False)
    start_date = models.DateField()
    signup_date = models.DateTimeField(auto_now_add=True, null=False)
    category = models.IntegerField(null=True)
    restrictions = models.TextField(default=None, blank=True, null=True)
    status = models.IntegerField()   # 0-pending 1-accepted etc.

    def __str__(self):
        return f"Volunteer: {self.name} Email: {self.email}"
    