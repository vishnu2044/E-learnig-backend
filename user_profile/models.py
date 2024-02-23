from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileImages(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='user_profile_images/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='user_cover_images/', null=True, blank=True)

    
    def __str__(self):
        return f"Profile image for {self.user.username}"