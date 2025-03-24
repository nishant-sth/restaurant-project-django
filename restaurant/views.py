from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import BookingForm
from django.views.generic import TemplateView
from django.core.mail import send_mail
# from rest_framework.decorators import api_view

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonials.objects.all()
        return context
    

def about(request):
    return render(request, 'about.html')



def menu(request):
    menu_data = Menu.objects.all()
    context = {
        'menu': menu_data
    }
    return render (request, 'menu.html', context)

def display_menu_item(request, pk):
    menu_item = Menu.objects.get(pk=pk)
    context = {
        'menu_item': menu_item
    }
    return render (request, 'menu_item.html', context)


# @api_view(['POST'])
def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            email_content = f"""
Thank you for making a reservation  
with our restaurant!  

This email is to confirm your upcoming reservation.  

RESERVATION DETAILS  
----------------------------  
Name: {form.cleaned_data['name']}  
Phone: {form.cleaned_data['phone_number']}  
Email: {form.cleaned_data['email']}  
Date & Time: {form.cleaned_data['booking_date']}  
Number of guests: {form.cleaned_data['no_of_guests']}  

We look forward to serving you!  

If you need to modify or cancel your reservation,  
please contact us at +1234567890.  
            """
            
            send_mail(
                'Reservation Confirmation',  # subject
                email_content,
                'settings.EMAIL_HOST_USER',  # sender email
                [form.cleaned_data['email']],  # receiver email
                fail_silently=False
            )
            messages.success(request, 'Your reservation has been confirmed! Please check your email.')
            return redirect('book')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm()
    
    context = {
        'form': form
    }
    return render(request, 'book.html', context)


