from django.shortcuts import redirect, render
from .models import users

def index(request):

    dict = {
        "users" : users.objects.all()
    }

    
    return render(request, "index.html" , dict )

def index2(request):
    

    if request.method == "POST":
    
        
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        age = request.POST["age"]


        users.objects.create(first_name= firstname,
        last_name= lastname,  email= email, age= age)


    return redirect("/")