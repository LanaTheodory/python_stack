from django.http import request
from django.shortcuts import render

def index(requests):
    return render(requests,'index.html')

def info(requests):
    
   name= requests.POST['name']
    email = requests.POST['email']
    location = requests.POST['location']
    language = requests.POST['language']
    comments = requests.POST['comments']

    data = {
       " name": name,
       "email":email,
       "location" : location,
       "language": language,
       "comments":comments
    }
    return render(requests, "info.html", data)