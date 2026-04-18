from django.db import models
from .tour import Tour

class Hotel(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=100)
    price_per_night = models.IntegerField()
    image = models.ImageField(upload_to='hotel_images/')
    description = models.TextField()

    def __str__(self):
        return self.name
    

