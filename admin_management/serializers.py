from rest_framework import serializers
from .models import EducationOptions, Professions

class EducationSerialzier(serializers.ModelSerializer):

    class Meta:
        model = EducationOptions
        fields = ('id', 'education')


class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professions
        fields = ('id', 'profession')