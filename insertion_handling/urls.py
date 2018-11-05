from django.urls import path
from . import views
urlpatterns = [
    path('new_ins/', views.new_insertion, name='new insertion'),
    path('<str:ins_id>/update_ins/', views.update_insertion, name='update insertion')
    ]