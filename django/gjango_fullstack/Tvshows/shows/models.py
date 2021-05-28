from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(default= 2020-8-12)
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def getshows():
    shows = Show.objects.all()
    return shows

def create( title,network,release_date, description ):
    Show.objects.create(title= title ,network= network ,release_date = release_date,  description= description)