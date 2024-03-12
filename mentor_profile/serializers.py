from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MentorProfile, Skills

class SignupMentorSerializer(serializers.Serializer):
    username = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.CharField()


class MenterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class MentorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MentorProfile
        fields = '__all__'


class MentorSkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ["skills", "id"]