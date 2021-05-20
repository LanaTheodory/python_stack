from django.shortcuts import render
import random

def index(request):
    request.session["rand"]= random.randint(1, 100) 
    return render(request, "index.html")	



def index2(request):
    print(request.session["rand"])
    if int(request.POST["guess"])  <  request.session["rand"]:
        return render(request, "index2.html")
    elif int(request.POST["guess"]) >  request.session["rand"]:
        return render(request, "index3.html")
    elif int(request.POST["guess"]) ==  request.session["rand"]:
        return render(request, "index4.html")
    
    


