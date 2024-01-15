from django.urls import path
from . import views
from postdetail.models import TeamArea, SingleTeamArea 

urlpatterns = [

    path("detail/<int:id>/", views.detailspost, name='detail'),

    path("breakingnewswidget/<int:id>/", views.breakingnewswidgetdetail, name="breakingnewswidget"),

    path("newsstreamdetail/<int:id>/", views.newsstreamdetail, name="newsstreamdetail"),

    path("gazettectaareadetail/<int:id>/", views.gazettectaareadetail, name="gazettectaareadetail"),

    path("aboutteamdetail/<int:id>/", views.aboutteamdetail, name="aboutteamdetail"),

    path("categorydetail/<int:id>/", views.categorydetail, name="categorydetail"),

    path("categorywelcomepostadetail/<int:id>/", views.categorywelcomepostadetail, name="categorywelcomepostadetail"),
    
    path("categorywelcomepostbdetail/<int:id>/", views.categorywelcomepostbdetail, name="categorywelcomepostbdetail"),


    path("categorywelcomepostcdetail/<int:id>/", views.categorywelcomepostcdetail, name="categorywelcomepostcdetail"),

    path("sportnewsdetailtop/<int:id>/", views.sportnewsdetailtop, name="sportnewsdetailtop"),

    path("sportnewsdetailmid/<int:id>/", views.sportnewsdetailmid, name="sportnewsdetailmid"),


    path("culturalnewsdetailtop/<int:id>/", views.culturalnewsdetailtop, name="culturalnewsdetailtop"),

    path("culturalnewsdetailmid/<int:id>/", views.culturalnewsdetailmid, name="culturalnewsdetailmid"),

    path("singlepostdetailtop/<int:id>/", views.singlepostdetailtop, name="singlepostdetailtop"),



    path("singlepostdetailmid/<int:id>/", views.singlepostdetailmid, name="singlepostdetailmid"),

    path("singleblogpostcontentdetailtop/<int:id>/", views.singleblogpostcontentdetailtop, name="singleblogpostcontentdetailtop"),
    
]

