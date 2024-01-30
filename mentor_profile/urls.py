from django.urls import path
from . import views 


urlpatterns = [
    path('signup-mentor-profile/', views.signup_mentor_profile, name='signup-mentor-profile'),
    path('mentor-login/', views.mentor_login, name='mentor-login'),
]
    