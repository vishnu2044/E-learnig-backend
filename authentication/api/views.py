from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from django.contrib.auth import authenticate


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add additional user information to the token payload
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username = username, password = password)

    if user is not None and user.is_superuser :
        admin_login_serializer = MyTokenObtainPairSerializer(data = {'username' : username, 'password': password})
        admin_login_serializer.is_valid(raise_exception=True)
        token_data = user.is_superuser

        return Response({
            'access' : token_data['access'],
            'refresh' : token_data['refresh'],
            'is_admin' : user.is_superuser,
        }, status= status.HTTP_200_OK)
    else:
        return Response({'error' : 'Invalid credentials'}, status= status.HTTP_401_UNAUTHORIZED)
    
    

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]
    return Response(routes)