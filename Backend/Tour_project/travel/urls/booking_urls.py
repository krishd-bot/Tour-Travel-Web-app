from django.urls import path
from travel.views.booking_views import bookingPanel

urlpatterns = [
    path('bookings/', bookingPanel),
]