from django import forms
from .models import Booking
from django.utils import timezone
from datetime import datetime
import re

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking       
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'no_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
            'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'comments': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or len(name.strip()) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long")
        return name.strip()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required")
        
        # Basic email format validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise forms.ValidationError("Please enter a valid email address")
        
        # Check for common disposable email domains
        disposable_domains = ['tempmail.com', 'throwawaymail.com', 'tempmailaddress.com']
        domain = email.split('@')[1].lower()
        if domain in disposable_domains:
            raise forms.ValidationError("Please use a permanent email address")
        
        return email.lower()

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone or len(phone) < 10:
            raise forms.ValidationError("Please enter a valid phone number")
        return phone

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        now = timezone.now()
        
        if booking_date < now:
            raise forms.ValidationError("Booking date cannot be in the past")
        
        if booking_date.hour < 9 or booking_date.hour >= 22:
            raise forms.ValidationError("Bookings can only be made between 9 AM and 10 PM")
        
        return booking_date

    


