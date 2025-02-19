from django.db import models
from django.core.exceptions import ValidationError
import os
from cloudinary.models import CloudinaryField
import cloudinary


class PageTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Heropage(models.Model):
    heading_text_1 = models.CharField(max_length=100)
    heading_underline_text_1 = models.CharField(max_length=100)
    heading_description_1 = models.TextField()
    heading_text_2 = models.CharField(max_length=100)
    heading_underline_text_2 = models.CharField(max_length=100)
    heading_description_2 = models.TextField()

    def __str__(self):
        return "Hero Section"
    
class About(models.Model):
    short_about = models.TextField()
    about_list_1=models.CharField(max_length=255)
    about_list_2=models.CharField(max_length=255)
    about_list_3=models.CharField(max_length=255)
    long_about = models.TextField()


class WhatOffered(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    RATE_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]

    name = models.CharField(max_length=50, null=False, blank=False)
    who_you_are = models.CharField(max_length=50, null=False, blank=False)
    rating = models.CharField(max_length=1, choices=RATE_CHOICES, null=False, blank=False)
    testimony = models.TextField(null=False, blank=False)
    user_image = CloudinaryField('image', blank=False, null=False)

    def delete(self, *args, **kwargs):
        if self.user_image:
            cloudinary.uploader.destroy(self.user_image.public_id)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Faq(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.question


def validate_audio_file(value):
    """Ensure the uploaded file is an audio format"""
    valid_extensions = ['.mp3', '.wav', '.ogg', '.flac', '.aac']
    
    # Skip validation if no new file is uploaded (Cloudinary URLs have no extensions)
    if isinstance(value, CloudinaryField) or not hasattr(value, 'name'):
        return

    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Only audio files are allowed! (MP3, WAV, OGG, FLAC, AAC)")

def validate_image_file(value):
    """Ensure the uploaded file is an image format"""
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    
    # Skip validation if no new file is uploaded
    if isinstance(value, CloudinaryField) or not hasattr(value, 'name'):
        return

    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Only image files are allowed! (JPG, PNG, GIF)")



class AudioFile(models.Model):
    name = models.CharField(max_length=50)
    file_cover = CloudinaryField('image', resource_type='image', blank=False, null=False, validators=[validate_image_file])
    file = CloudinaryField('audio', resource_type='raw', blank=False, null=False, validators=[validate_audio_file])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=50, choices=(('visible', 'visible'), ('hidden','hidden'), default='visible')

    def clean(self):
        """Only validate file fields if a new file is being uploaded"""
        if self.pk:  # If instance exists (update mode)
            old_instance = AudioFile.objects.get(pk=self.pk)
            if self.file_cover and self.file_cover != old_instance.file_cover:
                validate_image_file(self.file_cover)
            if self.file and self.file != old_instance.file:
                validate_audio_file(self.file)
        else:  # New instance
            validate_image_file(self.file_cover)
            validate_audio_file(self.file)

    def delete(self, *args, **kwargs):
        """Delete files from Cloudinary when instance is deleted"""
        if self.file_cover:
            cloudinary.uploader.destroy(self.file_cover.public_id)  # Delete image
        if self.file:
            cloudinary.uploader.destroy(self.file.public_id, resource_type="raw")  # Delete audio
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
