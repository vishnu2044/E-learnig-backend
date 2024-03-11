from django.urls import path
from . import views 


urlpatterns = [
    path('signup-mentor-profile/', views.signup_mentor_profile, name='signup-mentor-profile'),
    path('mentor-login/', views.mentor_login, name='mentor-login'),

    path('edit-mentor-profile/<int:user_id>/', views.edit_mentor_profile, name='edit-mentor-profile'),
    path('get-mentor-profile/<int:user_id>/', views.get_mentor_profile, name='get-mentor-profile'),

    path('update-skills/<int:user_id>/', views.update_skills, name='update-skills'),
    path('get-mentor-skills/<int:user_id>/', views.get_mentor_skills, name='get-mentor-skills'),


]
    