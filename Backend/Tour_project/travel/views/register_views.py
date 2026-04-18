from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from travel.serializers import Register_serializer

class RegisterView(APIView):
    def Post(self, request):
        serializer = regi