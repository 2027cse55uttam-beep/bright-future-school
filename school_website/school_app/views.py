from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Sab models ek hi line mein import kar diye
from .models import GalleryImage, HeroImage, AdmissionInquiry, ContactMessage

# Forms (agar nahi hai toh bana lena)
from .forms import AdmissionForm, ContactForm


# HOME PAGE
def home(request):
    gallery = GalleryImage.objects.all().order_by('-uploaded_at')[:9]
    hero_image = HeroImage.objects.first()  # Admin se set hero image
    return render(request, 'index.html', {
        'gallery': gallery,
        'hero_image': hero_image
    })


# ABOUT PAGE
def about(request):
    return render(request, 'about.html')


# ACADEMICS PAGE
def academics(request):
    return render(request, 'academics.html')


# ADMISSION PAGE
def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admission inquiry submitted successfully!")
            return redirect('admission_success')
    else:
        form = AdmissionForm()
    return render(request, 'admission.html', {'form': form})


# ADMISSION SUCCESS
def admission_success(request):
    return render(request, 'admission_success.html')


# GALLERY PAGE
def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})


# CONTACT PAGE - FULLY FIXED
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        # Message save in database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message_text
        )

        # Optional: Email to admin
        try:
            send_mail(
                f"New Contact: {subject}",
                f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message_text}",
                email,
                ['admin@brightfuture.edu.in'],  # Ya tera email daal de
                fail_silently=True,
            )
        except:
            pass  # Email fail ho toh bhi user ko success dikhao

        messages.success(request, "Thank you! Your message has been sent successfully. We will contact you soon!")
        return redirect('contact')

    return render(request, 'contact.html')


# CONTACT SUCCESS (agar alag page chahiye toh)
def contact_success(request):
    return render(request, 'contact_success.html')