# Generated by Django 5.1 on 2024-10-16 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(default='title', max_length=100)),
                ('card_desc', models.TextField()),
                ('link', models.TextField()),
                ('img_url', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medias.media')),
            ],
        ),
    ]
