from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.index),
    path('register' ,views.register),
    path('thoughts' , views.thoughts),
    path('addthought' , views.addthought),
    path('delete/<int:id>' , views.delete),
    path('thought/<int:id>' , views.thoughtid),
    path('like/<int:id>' , views.like),
    path('unlike/<int:id>' , views.unlike),
    path('login' , views.login),

    path('logout' , views.logout)
]