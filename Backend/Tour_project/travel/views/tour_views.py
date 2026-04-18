from rest_framework.decorators import api_view
from rest_framework.response import Response
from travel.models import Tour
from travel.serializers.tour_serializer import TourSerializer

@api_view(['GET'])
def getTours(request):
    tours = Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)