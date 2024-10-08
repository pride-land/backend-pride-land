# Generated by Django 5.1 on 2024-08-27 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('start_date', models.DateField()),
                ('signup_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.IntegerField(null=True)),
                ('restrictions', models.TextField(null=True)),
                ('status', models.IntegerField()),
            ],
        ),
    ]
