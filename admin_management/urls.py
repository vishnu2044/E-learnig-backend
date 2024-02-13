from django.urls import path
from . import views 


urlpatterns = [
    
    path('add-education/', views.add_education, name='add-education'),
    path('get-education-option-list/', views.get_education_option_list, name='get-education-option-list'),
    path('add-profession/', views.add_profession, name='add-profession'),
    path('get-profession-option-list/', views.get_profession_option_list, name='get-profession-option-list'),


]