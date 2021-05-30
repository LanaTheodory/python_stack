from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.index),
    path('register' ,views.register),
    path('welcome' , views.welcome),
    path('login' , views.login),
    path('addbook' , views.addbook),
    path('book/<int:id>' , views.bookdetails),
    path('update_book/<int:id>' , views.updatebook),
    path('delete_book/<int:id>' , views.deletebook),
    path("Un_fav/<int:id>" , views.unfavorite),
    path("add_to_fav/<int:id>" , views.addfav),

    path('logout' , views.logout)

]