
from rest_framework import serializers
from .models import AdminProfilePic


class AdminProfilePicSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = AdminProfilePic
        fields = ('user', 'profile_image')

    def get_profile_image(self, instance):
        if instance.profile_image:
            return self.context['request'].build_absolute_uri(instance.profile_image.url)
        return None
