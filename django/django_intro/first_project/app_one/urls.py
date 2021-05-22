
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path ('blogs', views.index),
    path('blogs/new',views.new),
    path('blogs/create', views.create),
    path('blogs/<int:x>', views.show),
    path('blogs/<int:x>/edit', views.edit),
    path('blogs/<int:x>/delete', views.destroy)
]