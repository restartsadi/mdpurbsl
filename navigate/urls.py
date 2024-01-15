from django.urls import path
from . import views
from . views import search


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us.html', views.about, name = 'about'),
    path('category.html', views.category, name = 'category'),
    path('contact.html', views.contact, name = 'contact'),
    path('single-post.html', views.singlepost, name = 'singlepost'),
    path('search.html', views.search, name='search'),
    path('culturalnews.html', views.culturalnews, name='culturalnews'),
    path('sportnews.html', views.sportnews, name ='sportnews'),
]