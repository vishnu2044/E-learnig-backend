from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupMentorSerializer

# Create your views here.
@api_view(['POST'])
def signup_mentor_profile(request):
    if request.method == "POST":
        serializer = SignupMentorSerializer(data = request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username = serializer.validated_data['username'],
                first_name = serializer.validated_data['firstname'],
                last_name = serializer.validated_data['lastname'],
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password1'],
                is_staff = True
            )
            print(">>>>>>>>>>>>>>>>>>>")
            print(">>>>>>>>>>>>>>>>>>>")
            print("serializer data :::", serializer)
            print(">>>>>>>>>>>>>>>>>>>")
            print("user ::::::::::::", user)
            print(">>>>>>>>>>>>>>>>>>>")
            print(">>>>>>>>>>>>>>>>>>>")

            return Response({"success" : "profile created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response({"error" : "User details not valid"}, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response({"error" : "the method is not POST"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


