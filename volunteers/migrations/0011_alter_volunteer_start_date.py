# Generated by Django 5.1 on 2024-09-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0010_alter_volunteer_signup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
