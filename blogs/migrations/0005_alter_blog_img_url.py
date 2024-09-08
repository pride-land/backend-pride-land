# Generated by Django 5.1 on 2024-09-07 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_title_blog_name_rename_blog_blog_text_and_more'),
        ('medias', '0016_media_alt_text_media_set_as_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img_url',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medias.media'),
        ),
    ]
