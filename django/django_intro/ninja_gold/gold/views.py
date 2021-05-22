from hashlib import new
from django.http import request
from django.shortcuts import redirect, render
import random 
from time import gmtime, strftime


def index(request):

    if "score" in request.session:
        score = request.session["score"]
    else:
        request.session["score"] = 0
        score = request.session["score"]

    if "string" in request.session:

        string = request.session["string"] 
    else:
        request.session["string"] = []
        string = request.session["string"] 


    dict = {
      
       'score' : score ,
       'string' : string,
       
    }

    return render(request , "index.html", dict )

def index2(request):
    time = strftime("%Y-%m-%d-%H:%M %p", gmtime())
   

    
    if request.POST["forms"] == "farm":
        randcave = random.randint(10,20)
        request.session["score"] += randcave
        
        request.session["string"].append(f"Earned {randcave} from the Farm! at {time}")
        
       

    if request.POST["forms"] == "cave":
        randcave = random.randint(5,10)
        request.session["score"] += randcave
        request.session["string"].append(f"Earned {randcave} from the Cave!  at {time}" )
        
        

    if request.POST["forms"] == "house":
        randhouse = random.randint(2,5)
        request.session["score"] += randhouse 
        request.session["string"].append(f"Earned {randhouse } from the House!  at {time}" )


    if request.POST["forms"] == "casino":
        randcasino = random.randint(-50,50)
        request.session["score"] += randcasino
        
        if randcasino > 0:
            request.session["string"].append(f"Earned {randcasino} from the Casino!  at {time}") 
            
        else:
            
            
            request.session["string"].append( f"You have lost {randcasino} from the Casino!  at {time}" )

    

    return redirect("/")

def index3(request):
    request.session.clear()
    
    return redirect("/")