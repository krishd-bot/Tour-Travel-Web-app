from rest_framework import serializers
from travel.models import Tour, Hotel

class HotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
    
class TourSerializer(serializers.ModelSerializer):
    hotels = HotalSerializer(many=True, read_only=True)
    class Meta:
        model = Tour
        fields = "__all__"