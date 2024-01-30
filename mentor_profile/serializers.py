from rest_framework import serializers

class SignupMentorSerializer(serializers.Serializer):
    username = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.CharField()