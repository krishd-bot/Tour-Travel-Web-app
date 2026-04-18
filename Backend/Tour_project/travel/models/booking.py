from django.db import models
from .tour import Tour
from .hotel import Hotel

class Booking(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=10)
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    nights = models.IntegerField()
    total_price = models.IntegerField()

    def save(self, *args, **kwargs):
        self.total_price = self.hotels.price_per_night * self.nights
        super().save(*args, **kwargs)
    

