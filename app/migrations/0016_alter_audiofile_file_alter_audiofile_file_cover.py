# Generated by Django 5.1.6 on 2025-02-08 09:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_audiofile_file_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='audio'),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='file_cover',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
