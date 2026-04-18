from django.urls import path
from travel.views.tour_views import getTours

urlpatterns = [
    path('tour/', getTours)
]
