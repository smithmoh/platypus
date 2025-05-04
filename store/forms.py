from django import forms
from .models import EventInquiry, Contact

class EventInquiryForm(forms.ModelForm):
    class Meta:
        model = EventInquiry
        fields = ['event_date', 'event_type', 'budget', 'details', 'guest_count']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'details': forms.Textarea(attrs={'rows': 4}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }