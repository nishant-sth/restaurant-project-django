import qrcode
import io
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import BookingForm
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from .utils import render_to_pdf
from datetime import datetime
import base64
from barcode.writer import ImageWriter
from barcode import Code128

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



def send_reservation_confirmation(reservation, form_data):
    qr_data = f"""
    Restaurant Reservation
    ----------------------
    Name: {form_data['name']}
    Date: {form_data['booking_date']}
    Guests: {form_data['no_of_guests']}
    Reservation ID: {reservation.id}
    Phone Number: {form_data['phone_number']}
    """
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    html_content = render_to_string('reservation_email.html', {
        'reservation': reservation,
        'qr_code': buffer.read().hex()
    })
    
    email = EmailMessage(
        'Reservation Confirmation', #subject
        html_content, #body
        'settings.EMAIL_HOST_USER', #sender email address
        [form_data['email']], # email address to the recipient list
    )
    email.content_subtype = "html"
    email.attach('reservation_qr.png', buffer.getvalue(), 'image/png')
    email.send()

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            send_reservation_confirmation(reservation, form.cleaned_data)
            messages.success(request, 'Your reservation has been confirmed! Please check your email.')
            
            return render(request, 'book.html', {
                'form': BookingForm(),
                'booking_id': reservation.id
            })
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm()
    
    return render(request, 'book.html', {'form': form})

class GeneratePdf(View):
    def get(self, request, booking_id, *args, **kwargs):
        try:
            booking = Booking.objects.get(id=booking_id)
            
            # Generate barcode
            booking_code = f"BK{booking.id:04d}" #booking code
            buffer = io.BytesIO()
            Code128(booking_code, writer=ImageWriter()).write(buffer)
            barcode_data = base64.b64encode(buffer.getvalue()).decode()
            
            context = {
                'booking': booking,
                'today': datetime.now(),
                'barcode': barcode_data,
                'booking_code': booking_code
            }
            
            if pdf := render_to_pdf('pdf.html', context):
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = f"EliteKitchen_Booking_{booking.name}.pdf"
                
                # Check if download parameter is present
                if request.GET.get('download'):
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                else:
                    response['Content-Disposition'] = f'inline; filename="{filename}"'
                
                return response
            return HttpResponse("Error generating PDF")
        except Booking.DoesNotExist:
            return HttpResponse("Booking not found")