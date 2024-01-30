from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupMentorSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate



# Create your views here.
class MentorTokenObtainSerialzer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        if user.is_staff:
            token['is_staff'] = True

        return token


@api_view(['POST'])
def signup_mentor_profile(request):
    if request.method == "POST":
        serializer = SignupMentorSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username = serializer.validated_data['username'],
                first_name = serializer.validated_data['firstname'],
                last_name = serializer.validated_data['lastname'],
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password1'],
                is_staff = True
            )
            return Response({"success" : "profile created successfully"}, status=status.HTTP_201_CREATED)

        return Response({"error" : "User details not valid"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"error" : "the method is not POST"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def mentor_login(request):
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username = username, password = password)

        if user is not None and user.is_staff:
            mentor_login_serializer = MentorTokenObtainSerialzer(data = {'username': username, 'password': password})
            mentor_login_serializer.is_valid(raise_exception=True)
            token_data = mentor_login_serializer.validated_data

            return Response({
                "access": token_data['access'],
                'refresh': token_data['refresh'],
                'is_staff': user.is_staff
            }, status= status.HTTP_200_OK)
        else:
            return Response({"error": "invalied credentials"}, status=status.HTTP_400_BAD_REQUEST)