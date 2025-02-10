# Generated by Django 5.1.6 on 2025-02-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_audiofile_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiofile",
            name="genre",
            field=models.CharField(
                choices=[("Gospel", "gospel"), ("Afro", "Afro"), ("Other", "Other")],
                default="Gospel",
                max_length=255,
            ),
        ),
    ]
