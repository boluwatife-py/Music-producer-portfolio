# Generated by Django 5.1.6 on 2025-02-08 08:13

import app.models
import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_alter_audiofile_file_alter_audiofile_file_cover"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="audiofile",
            name="file_cover",
        ),
        migrations.AlterField(
            model_name="audiofile",
            name="file",
            field=cloudinary.models.CloudinaryField(
                max_length=255,
                validators=[app.models.validate_audio_file],
                verbose_name="audio",
            ),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="user_image",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="image"
            ),
        ),
    ]
