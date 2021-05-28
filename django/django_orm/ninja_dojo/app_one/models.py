from django.db import models
from django.db.models.fields import TextField



class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo= models.ForeignKey( Dojo, related_name="dojo", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def result(form):
    Dojo.objects.create(name = form["name"] , city = form["city"] , state = form["state"])

def result2(form):
    print(form["select"])
   
    Ninja.objects.create(first_name = form["first_name"] , last_name = form["last_name"] , dojo = Dojo.objects.get(name=form["select"]) )
