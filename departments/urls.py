from django.urls import path
from . import views 


urlpatterns = [
    path('add-department/', views.add_department, name='add-department'),
    path('get-departments/', views.get_all_departments, name='get-departments'),
    path('edit-department/', views.edit_department, name='edit-department'),

]
    