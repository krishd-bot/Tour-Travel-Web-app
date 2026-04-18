from rest_framework.decorators import api_view
from rest_framework.response import Response

from travel.serializers.booking_serializer import BookingSerializer

@api_view(['POST'])
def bookingPanel(request):
    serializer = BookingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)