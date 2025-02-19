from django.contrib import admin
from .models import Heropage, PageTitle, About, WhatOffered, Testimonial, Faq, AudioFile
from django.core.exceptions import ValidationError
from django.contrib import messages

class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in Testimonial._meta.fields]

    def has_add_permission(self, request):
        return False  # Disable adding new testimonials

    def has_change_permission(self, request, obj=None):
        return False  # Disable editing existing testimonials

    def has_delete_permission(self, request, obj=None):
        return True  # Disable deleting testimonials

admin.site.register(Testimonial, TestimonialAdmin)

admin.site.register(Faq)

class AudioFileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()  # Validate model fields before saving
            super().save_model(request, obj, form, change)
            messages.success(request, "Audio file saved successfully!")  # Success message
        except ValidationError as e:
            messages.error(request, "Error: " + " ".join(e.messages))  # Show clean error message
        except Exception:
            messages.error(request, "An unexpected error occurred. Please check your file format and try again.")

class Home(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Heropage, Home)
admin.site.register(About, Home)
admin.site.register(WhatOffered, Home)
