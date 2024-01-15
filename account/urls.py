from django.urls import path
from . import views

urlpatterns = [
    #path("register", views.register, name="register"),
    #path("login", views.login, name="login"),
    #path("logout", views.logout, name="logout"),
    path("subscribe" , views.subscribe, name="subscribe"),
    path("comment", views.comment, name="comment"),
]