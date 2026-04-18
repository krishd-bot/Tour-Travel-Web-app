from rest_framework.decorators import api_view
from rest_framework.response import Response
from travel.models import Hotel
from travel.serializers.tour_serializer import HotalSerializer

@api_view(['GET'])
def getHotels(request):
    hotels = Hotel.objects.all()
    serializer = HotalSerializer(hotels, many=True)
    return Response(serializer.data)