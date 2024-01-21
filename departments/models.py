from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length = 250, blank=True, null=True )
    image = models.ImageField(upload_to='department_images',blank=True, null=True)
    total_teachers = models.CharField(max_length = 250, blank=True, null=True )
    total_students = models.CharField(max_length = 250, blank=True, null=True )
    created_time = models.DateTimeField(auto_now_add=True)
    













