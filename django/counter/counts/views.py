from django.shortcuts import redirect, render 

def index(requests):
    
    counter =  requests.session.get("count" ,1)

    requests.session["count"] = counter +1
     
    dict ={

        "counts": counter
    }


     
    
    # if "count" in  requests.session:
        
    #     requests.session["count"] += 1

    # counts = requests.session["count"] 
    
    # dict ={

    #     "counts": counts
    # }
    
    return render(requests, "index.html", dict )
   

def index2(requests):
    requests.session.clear()
    return redirect("/")
    
def index3(requests):
    requests.session["count"] += 1
    return redirect("/")



   