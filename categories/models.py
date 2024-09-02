from django.db import models

class Categories(models.Model):
    bamboo = models.BooleanField(default=False)
    vegetables = models.BooleanField(default=False)
    eggs = models.BooleanField(default=False)
    shiitake = models.BooleanField(default=False)
    bees = models.BooleanField(default=False)
    goats = models.BooleanField(default=False)
    construction = models.BooleanField(default=False)
   

    def __str__(self):
        return f"Categories List: {self.id}"
      

