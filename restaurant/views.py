from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import BookingForm
from django.views.generic import TemplateView
from django.core.mail import send_mail
import qrcode
import io
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
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
            
            # Prepare reservation details for QR code
            qr_data = f"""
Restaurant Reservation
----------------------
Name: {form.cleaned_data['name']}
Date: {form.cleaned_data['booking_date']}
Guests: {form.cleaned_data['no_of_guests']}
Reservation ID: {reservation.id}
"""
            # Generate QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save QR code to a bytes buffer
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            
            # HTML email template
            html_content = render_to_string('reservation_email.html', {
                'reservation': reservation,
                'qr_code': buffer.read().hex()  # Pass the image data
            })
            
            # Create and send email
            email = EmailMessage(
                'Reservation Confirmation',
                html_content,
                'settings.EMAIL_HOST_USER',
                [form.cleaned_data['email']],
            )
            email.content_subtype = "html"  # Set content to HTML
            email.attach('reservation_qr.png', buffer.getvalue(), 'image/png')
            email.send()
            
            messages.success(request, 'Your reservation has been confirmed! Please check your email.')
            return redirect('book')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm()
    
    return render(request, 'book.html', {'form': form})