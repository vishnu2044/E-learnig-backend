from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminProfilePic(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='admin_profile_images',blank=True, null=True)


