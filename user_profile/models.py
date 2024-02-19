from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileImages(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField( upload_to='user_profile_img',blank=True, null=True)
    cover_image = models.ImageField(upload_to='user_cover_image',blank=True, null=True)