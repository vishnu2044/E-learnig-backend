from django.urls import path
from . import views 


urlpatterns = [
    path('upload-profile-image/', views.upload_profile_image, name='upload-profile-image'),
    path('get-profile-img/<int:user_id>/', views.get_profile_img, name='get-profile-img'),

]
    