from django import forms
from .models import AdmissionInquiry

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionInquiry
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))