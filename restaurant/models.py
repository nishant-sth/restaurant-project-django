from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)
    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, default='test@test.com')
    phone_number = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    comments = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField(max_length=1000)
    role = models.CharField(max_length=200)
    rating = models.IntegerField( 
        default=3,
        validators=[
            MaxValueValidator(5)   # Maximum value of 5
        ]
    )

    def __str__(self):
        return self.name
