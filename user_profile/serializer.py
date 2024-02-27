from rest_framework import serializers
from . models import UserProfileImages

class UserImagesSerializer(serializers.ModelSerializer):
    profile_img_url = serializers.SerializerMethodField()
    cover_img_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileImages
        fields = ['profile_img_url', 'cover_img_url']
        
    def get_profile_img_url(self, obj):
        if obj.profile_image:
            return obj.profile_image.url
        return None
    
    def get_cover_img_url(self, obj):
        if obj.cover_image:
            return obj.cover_image.url
        return None
