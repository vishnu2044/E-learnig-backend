from django.db import models

# Create your models here.
class Professions(models.Model):
    id = models.AutoField(primary_key=True)
    profession = models.CharField(max_length = 255, null=True, blank=True)

class EducationOptions(models.Model):
    id = models.AutoField(primary_key=True)
    education = models.CharField(max_length = 255, null=True, blank=True)
    


