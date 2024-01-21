from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import AdminProfilePic
from .serializer import AdminProfilePicSerializer


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def edit_admin_profile(request):
    current_user = request.user


    if current_user:
        print("admin is a super user")
        
        username = request.data.get('username')
        first_name = request.data.get("first_name")
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        profile_image = request.data.get('profileImg')


        try:
            profile = AdminProfilePic.objects.get(user=current_user)
        except AdminProfilePic.DoesNotExist:
            profile = AdminProfilePic(user=current_user)

        profile.profile_image = profile_image
        profile.save()

        current_user.username = username
        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.email = email
        current_user.save()

        
        return Response({'success': 'updated successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'user not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_admin_profile_pic(request):
    current_user = request.user

    if current_user.is_superuser:
        try:
            profile = AdminProfilePic.objects.get(user = current_user)
            serializer = AdminProfilePicSerializer(profile, context={'request': request})
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except AdminProfilePic.DoesNotExist:
            return Response({'error': 'image is not present'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'user not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    