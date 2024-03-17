from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import EducationOptions, Professions
from rest_framework import status
from rest_framework.response import Response
from .serializers import EducationSerialzier, ProfessionSerializer

# Create your views here.
# Education management >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_education(request):
    if request.method == "POST":
        try:
            education = request.data.get("education")
            check = EducationOptions.objects.filter(education = education)
            if check:
                return Response({'error': 'already presenet'}, status=status.HTTP_409_CONFLICT)
            else:
                if education:
                    EducationOptions.objects.create(
                        education = education
                    )
                    return Response({"success": "data added"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Input is empty : bad request"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "Internal server Error!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_education_option_list(request):
    try:
        profession_list = EducationOptions.objects.all()
        serializer = EducationSerialzier(profession_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Professions.DoesNotExist:
        return Response({"error" : "Educational details are empty"}, status=status.HTTP_404_NOT_FOUND)



#Porfession management >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_profession(request):
    if request.method == "POST":
        try:
            profession = request.data.get("profession")
            check = Professions.objects.filter(profession = profession)
            if check:
                return Response({'error': 'already presenet'}, status=status.HTTP_409_CONFLICT)
            else:
                if profession:
                    Professions.objects.create(
                        profession = profession
                    )
                    return Response({"success": "data added"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Title and body are required"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profession_option_list(request):
    try:
        profession_list = Professions.objects.all()
        serializer = ProfessionSerializer(profession_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except EducationOptions.DoesNotExist:
        return Response({"error" : "professional detailss are empty"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_profession(request, profession_id):
    try:
        Professions.objects.get(id = profession_id).delete()
        return Response({"success": "data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Professions.DoesNotExist:
        return Response({'error': 'data does not excists' }, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_education(request, edu_id):
    try:
        EducationOptions.objects.get(id = edu_id).delete()
        return Response({'success': 'data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    except EducationOptions.DoesNotExist:
        return Response({'error': 'data does not excists' }, status=status.HTTP_404_NOT_FOUND)