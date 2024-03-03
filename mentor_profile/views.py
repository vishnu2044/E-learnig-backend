from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
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
        token['id'] = user.id
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        

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

        # Check if the user is a superuser first
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            mentor_login_serializer = MentorTokenObtainSerialzer(data={'username': username, 'password': password})
            mentor_login_serializer.is_valid(raise_exception=True)
            token_data = mentor_login_serializer.validated_data
            return Response({
                "access": token_data['access'],
                'refresh': token_data['refresh'],
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        


def get_mentor_profile(request):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_mentor_profile(request, user_id):
    if request.method == "POST":
        username = request.POST.get("username")
        education = request.POST.get("education")
        profession = request.POST.get("profession")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        skills = request.POST.get("skills")
        print("skils :::::::::::::::", skills)


        return Response({"success": "data get"}, status= status.HTTP_200_OK)
    else:
        return Response({"error": "method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)