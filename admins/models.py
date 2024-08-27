from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.TextField(null=False)
    email = models.EmailField(max_length=254)
    status = models.TextField(null=True)

    def __str__(self):
        return f"admin: {self.name}, email: {self.email}, status: {self.status}"