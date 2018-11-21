from django.urls import path
from . import views
from . import forms
from django.contrib.auth.views import LoginView, LogoutView
from profile_handling.forms import UtenteLoginForm

urlpatterns= [
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(authentication_form=UtenteLoginForm), name= 'profile_handling'),
    path('logout/', LogoutView.as_view(next_page='home'), name= 'logout')    
    ]