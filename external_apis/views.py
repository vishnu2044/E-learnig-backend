from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from decouple import config
from rest_framework.response import Response
from rest_framework import status
from requests import get as http_get

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def google_places(request):
    input_value = request.GET.get("input")
    API_KEY = config('GOOGLE_API_KEY', default='')
    if not API_KEY:
        print("api not foundd")
        return Response({"error": "api key not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if input_value:
        try:
            response = http_get(
                f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={input_value}&key={API_KEY}"
            )   
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except :
            return Response({"error": "get some error from backend"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({"error": "Input value required"}, status=status.HTTP_400_BAD_REQUEST)