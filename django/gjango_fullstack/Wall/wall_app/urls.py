from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register' ,views.register),
    path('wall', views.main_wall),
    path('login' , views.login),
    path('addmessage', views.addmessage),
    path('addcomment', views.addcomment),
    path('logout' , views.logout),
    path('deletecomment' , views.delete),

]
