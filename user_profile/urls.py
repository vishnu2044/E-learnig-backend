from django.urls import path
from . import views 


urlpatterns = [
    path('upload-profile-image/', views.upload_profile_image, name='upload-profile-image'),
    path('get-profile-img/<int:user_id>/', views.get_profile_img, name='get-profile-img'),

    path('upload-cover-image/', views.upload_cover_image, name='upload-cover-image'),
    path('get-cover-img/<int:user_id>/', views.get_cover_img, name='get-cover-img'),

]
    