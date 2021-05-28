from django.db import models
import datetime
from datetime import *

class BlogManager(models.Manager):

    def basic_validator(self, title, network , release_date, description):
        datenow =datetime.now().strftime("%Y-%m-%d ")
 
        errors = {}
        if len(title) < 2:
            errors["title"] = "show title should be at least 2 characters"
        if len( network) < 3:
            errors["network"] = "show network should be at least 3 characters"
        if len(description) < 10:
            errors["description"] = "show description should be at least 10 characters"
        if release_date > datenow:
            errors["release_date"] = "show release date should be in the past"
        return errors
       


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(default= 2020-8-12)
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

def getshows():
    shows = Show.objects.all()
    return shows

def create( title,network,release_date, description ):
    Show.objects.create(title= title ,network= network ,release_date = release_date,  description= description)