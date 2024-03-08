from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MentorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15,null=True)
    education = models.TextField(null=True)
    profession = models.TextField(null=True)
    place = models.CharField(max_length=255,null=True)
    industrialExperience = models.TextField(null=True)
    teachingExperience = models.TextField(null=True)
    selfIntro = models.TextField(null=True)


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.TextField(null=True)
