from django.urls import path
from travel.views.hotel_views import getHotels

urlpatterns = [
    path('hotels/', getHotels),
]