from django.db import models
import django.utils.timezone

# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(null=False)
    email = models.EmailField(null=False)
    start_date = models.DateTimeField()
    signup_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='sign up date')
    bamboo = models.BooleanField(default=False)
    vegetables = models.BooleanField(default=False)
    eggs = models.BooleanField(default=False)
    shiitake = models.BooleanField(default=False)
    bees = models.BooleanField(default=False)
    goats = models.BooleanField(default=False)
    construction = models.BooleanField(default=False)
    restrictions = models.TextField(default=None, blank=True, null=True)
    is_accepted = models.BooleanField(default=False, help_text='Designates whether this volunteer is accepted. Review then accept', verbose_name='active')

    def __str__(self):
        return f"Volunteer: {self.name} Email: {self.email}"
    