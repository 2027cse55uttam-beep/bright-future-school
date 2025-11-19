from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admission/', views.admission, name='admission'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('admission-success/', views.admission_success, name='admission_success'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('admission/', views.admission, name='admission'),
    path('admission-success/', views.admission_success, name='admission_success'),
   path('contact/', views.contact, name='contact'),
]