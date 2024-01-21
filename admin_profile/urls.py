from django.urls import path
from . import views 


urlpatterns = [
    
    path('edit-admin-profile/', views.edit_admin_profile, name='edit-admin-profile'),
    path('get-admin-profile-pic/', views.get_admin_profile_pic, name='get-admin-profile-pic'),

]