from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    # path('menu_item/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('book/', book, name='book'),
    # path('pdf/', GeneratePdf.as_view(), name='pdf'),
    path('booking/<int:booking_id>/pdf/', GeneratePdf.as_view(), name='booking_pdf'),
]


