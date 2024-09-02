from django.db import models
import django.utils.timezone

# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(null=False)
    email = models.EmailField(null=False)
    start_date = models.DateField()
    signup_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='sign up date')
    category = models.IntegerField(null=True, help_text="1-Weeds, 2-Shittake Mushrooms, 3-Eggs, 4-Bee Keeping, 5-Bamboo")
    restrictions = models.TextField(default=None, blank=True, null=True)
    is_accepted = models.BooleanField(default=False, help_text='Designates whether this volunteer is accepted. Review then accept', verbose_name='active')

    def __str__(self):
        return f"Volunteer: {self.name} Email: {self.email}"
    