# Generated by Django 5.1.6 on 2025-02-07 23:08

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_remove_audiofile_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiofile",
            name="file",
            field=models.FileField(
                upload_to="audio_files/", validators=[app.models.validate_audio_file]
            ),
        ),
        migrations.AlterField(
            model_name="audiofile",
            name="file_cover",
            field=models.ImageField(
                upload_to="Audio", validators=[app.models.validate_image_file]
            ),
        ),
    ]
