from django.urls import path
from . import views 


urlpatterns = [
    path('signup-mentor-profile/', views.signup_mentor_profile, name='signup-mentor-profile'),
]
    