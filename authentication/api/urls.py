from django.urls import path
from . import views 
from .views import MyTokenObtainPairView, check_user_is_admin, check_user_is_mentor

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("token/check-user-is-admin", check_user_is_admin, name='check-user-is-admin'),
    path("token/check-user-is-mentor", check_user_is_mentor, name='check-user-is-mentor')
]
    