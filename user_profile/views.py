from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserProfileImages
from .serializer import UserImagesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
import base64
from django.contrib.auth.models import User
from django.http import HttpResponse
import uuid
from django.http import FileResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_image(request):
    if request.method == "POST":
        user = request.user
        print("user:::::::::::", user.username)
        profile_img = request.FILES.get("profile_img") 
        
        if profile_img:
            print(">>>>>>>>>>>>>>>>>>>")
            print(">>>>>>>>>>>>>>>>>>>")
            print(len(profile_img))
            print(">>>>>>>>>>>>>>>>>>>")
            print(">>>>>>>>>>>>>>>>>>>")
            # Generate a unique filename
            unique_filename = f"profile_image_{uuid.uuid4().hex}.jpg"
            print(">>>>>>>>>>>>>>>>>>>")
            print(">>>>>>>>>>>>>>>>>>>")
            print(len(unique_filename))
            print(">>>>>>>>>>>>>>>>>>>")
            print(">>>>>>>>>>>>>>>>>>>")
            print("image unique name:::::::::", unique_filename)
            try:
                data = UserProfileImages.objects.get(user=user)
            except UserProfileImages.DoesNotExist:
                data = UserProfileImages.objects.create(user=user)

            # Assign the unique filename to the image
            data.profile_image.save(unique_filename, profile_img)
            data.save()
            return Response({"success": "Profile updated successfully"}, status=status.HTTP_200_OK)
        else:
            print("image is not found!!!!")
            print("image is not found!!!!")
            print("image is not found!!!!")
            print("image is not found!!!!")
            raise ParseError("Image not found")
    else:
        return Response({"error": "User not authorized"})



@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def get_profile_img(request, user_id):
    try:
        user_profile = UserProfileImages.objects.get(user=user_id)
        serializer = UserImagesSerializer(user_profile)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except ObjectDoesNotExist:
        return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

    
