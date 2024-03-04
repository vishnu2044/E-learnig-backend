from django.urls import path
from . import views 


urlpatterns = [
    path('google-places/', views.google_places, name='google-places'),
]
    