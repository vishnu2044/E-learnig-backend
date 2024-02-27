from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserProfileImages
from .serializer import UserImagesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from django.contrib.auth.models import User
import uuid
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_image(request):
    if request.method == "POST":
        user = request.user
        profile_img = request.FILES.get("profile_img") 
        if profile_img:
            unique_filename = f"profile_image_{user.username}_{user.id}.jpg"
            try:
                data = UserProfileImages.objects.get(user=user)
            except UserProfileImages.DoesNotExist:
                data = UserProfileImages.objects.create(user=user)
            # Assign the unique filename to the image
            data.profile_image.save(unique_filename, profile_img)
            data.save()
            return Response({"success": "Profile updated successfully"}, status=status.HTTP_200_OK)
        else:
            raise ParseError("Image not found")
    else:
        return Response({"error": "Method not allowed"})



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

    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_cover_image(reqeust):
    if reqeust.method == "POST":
        user = reqeust.user
        cover_img = reqeust.FILES.get("cover_img")
        if cover_img:
            unique_file_name = f"cover_img_{user.username}_{user.id}.jpg"
            try:
                data = UserProfileImages.objects.get(user = user)
            except UserProfileImages.DoesNotExist:
                data = UserProfileImages.objects.create(user = user)
            data.cover_image.save(unique_file_name, cover_img)
            data.save()
            return Response({"success": "Cover image saved successfully"}, status=status.HTTP_200_OK)
        else:
            raise ParseError("image not found")
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_502_BAD_GATEWAY)
    
    
@api_view(["GET"]) 
@permission_classes([IsAuthenticated])
def get_cover_img(reqeust, user_id):
    try:
        data = UserProfileImages.objects.get(user = user_id)
        if data:
            serializer = UserImagesSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    except ObjectDoesNotExist:
        return Response({'error': 'Cover image not found'}, status=status.HTTP_404_NOT_FOUND)
