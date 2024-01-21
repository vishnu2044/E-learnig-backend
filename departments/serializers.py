from rest_framework import serializers
from .models import Departments


class DepartmentSerializer(serializers.ModelSerializer):
    department_image = serializers.SerializerMethodField()

    class Meta:
        model = Departments
        fields = ('name','id', 'department_image', 'total_teachers', 'total_students', 'created_time')

    def get_department_image(self, instance):
        if instance.image:
            return self.context['request'].build_absolute_uri(instance.image.url)
        return None

