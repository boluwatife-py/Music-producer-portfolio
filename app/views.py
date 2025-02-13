from django.shortcuts import render, redirect
from .models import Heropage, PageTitle, About, WhatOffered, Testimonial, Faq, AudioFile
from django.contrib import messages

def home(request):
    title = PageTitle.objects.first()
    heroitems = Heropage.objects.first()
    about = About.objects.first()
    whatoffered = WhatOffered.objects.all()
    audios = AudioFile.objects.all().order_by('-id')

    context = {
        'title': title.title,
        'heading_text_1': heroitems.heading_text_1,
        'heading_underline_text_1': heroitems.heading_underline_text_1,
        'heading_description_1': heroitems.heading_description_1,
        'heading_text_2': heroitems.heading_text_2,
        'heading_underline_text_2': heroitems.heading_underline_text_2,
        'heading_description_2': heroitems.heading_description_2,
        'short_about': about.short_about,
        'about_list_1': about.about_list_1,
        'about_list_2': about.about_list_2,
        'about_list_3': about.about_list_3,
        'long_about': about.long_about,
        'testimonials': Testimonial.objects.all(),
        'faq': Faq.objects.all(),
        'audios': audios
    }
    for i, item in enumerate(whatoffered, start=1):
        context['what_offered_title_%s' %i] = item.title
        context['what_offered_description_%s' %i] = item.description
    
    return render(request, "index.html", context)


def make_review(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        who_you_are = request.POST.get("who_you_are", "").strip()
        rating = request.POST.get("rating", "").strip()
        testimony = request.POST.get("testimony", "").strip()
        user_image = request.FILES.get("user_image")

        # Validate required fields
        if not all([name, who_you_are, rating, testimony]):
            messages.error(request, "All fields are required!")
            return render(request, "review.html")

        # Validate rating choice
        valid_ratings = [choice[0] for choice in Testimonial.RATE_CHOICES]
        if rating not in valid_ratings:
            messages.error(request, "Invalid rating selected!")
            return render(request, "review.html")

        # Validate image
        if not user_image:
            messages.error(request, "Please upload an image.")
            return render(request, "review.html")

        try:
            # Create a testimonial instance and validate it
            testimonial = Testimonial(
                name=name,
                who_you_are=who_you_are,
                rating=rating,
                testimony=testimony,
                user_image=user_image
            )
            testimonial.full_clean()  # Runs model validation
            testimonial.save()

            messages.success(request, "Your review has been submitted successfully!")
            return redirect("home")

        except ValidationError as e:
            messages.error(request, " ".join(e.messages))

    return render(request, "review.html")