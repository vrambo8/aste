from django.urls import path
from . import views

urlpatterns= [
    path('', views.home_page, name="home"),
    path('feed/', views.page, name="feed"),
    
    ]