from rest_framework import serializers
from travel.models import Hotel

class HotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"