from django.contrib import admin
from .models import GalleryImage, HeroImage, ContactMessage, AdmissionInquiry

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)
    list_per_page = 20

@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at', 'is_read')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'sent_at')
    list_filter = ('is_read', 'sent_at')

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(AdmissionInquiry)