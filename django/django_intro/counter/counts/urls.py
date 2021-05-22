from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('destroy' , views.index2),
    path('add2' , views.index3)
]

