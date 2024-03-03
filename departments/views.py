from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Departments
from rest_framework.decorators import api_view, permission_classes
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .pagination import DepartmentPagination

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_department(request):
    if request.method != 'POST':
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    user = request.user
    if user.is_superuser:
        department_name = request.data.get('departmentName')
        if 'department_img' in request.FILES:
            department_img = request.FILES['department_img']
        if Departments.objects.filter(name=department_name).exists():
            return Response({'error': 'Department already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            Departments.objects.create(name=department_name, image = department_img)
            return Response({'success': 'Department added successfully!'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User is not an admin'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def edit_department(request, department_id):
    user = request.user
    if user.is_superuser:
        if request.method != 'POST':
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            department_name = request.POST.get("departmentName")
            if 'department_img' in request.FILES:
                department_img = request.FILES['department_img']
            else:
                department_img = None
            try:
                department = Departments.objects.get(id = department_id)
                department.name = department_name
                if department_img:
                    department.image = department_img
                department.save()
                return Response({"success" : 'department updated successfully'}, status=status.HTTP_200_OK)
            except:
                pass          
    else:
        return Response({'error': 'User is not an admin'}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_departments(request):

    user = request.user
    if user.is_superuser:
        departments = Departments.objects.all()
        paginator = DepartmentPagination()
        result_page = paginator.paginate_queryset(departments, request)
        serializer = DepartmentSerializer(result_page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)  
    
    else:
        return Response({"error": "user is not admin"}, status=status.HTTP_401_UNAUTHORIZED)
