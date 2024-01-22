from rest_framework import serializers

class SignupMentorSerializer(serializers.Serializer):
    username = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    email = serializers.CharField()