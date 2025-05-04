from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False, help_text="Optional: Provide an email address.")
    phone_number = forms.CharField(max_length=15, required=False, help_text="Optional: Provide a phone number (e.g., +254123456789).")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise forms.ValidationError("You must provide either an email or a phone number.")

        if email and CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        if phone_number and CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered.")

        return cleaned_data