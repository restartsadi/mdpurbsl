from django.urls import path
from video import views

urlpatterns = [
     path('', views.video, name='video'),
     
]