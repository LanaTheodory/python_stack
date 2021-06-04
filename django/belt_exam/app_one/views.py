
from django.shortcuts import redirect, render 
from . import models
from django.contrib import messages
import bcrypt





def index(request):


    if "id" in request.session:
        return redirect('/thoughts')
    else:

        return render(request,"index.html")

def thoughts(request):

    if "id" not in request.session:
        return redirect('/')
    else:
        context ={
            "all_thoughts": models.get_all_thoughts()
   
        }
        return render(request,"welcome.html" , context)
        

def register(request):
  
    errors = models.User.objects.basic_validator(request.POST)
    

    if len(errors) > 0:
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
      
        if request.method == "POST" :
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            Email = request.POST['Email']
            passwd = request.POST['passwd']
            conpasswd = request.POST['conpasswd']
            

            if models.check_password(passwd, conpasswd)  :
                hashed_passwd = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
                user = models.create_user(first_name ,last_name , Email , hashed_passwd)
                if "id" not in request.session:
                    request.session['id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name 
                    return redirect('/thoughts')
    return redirect('/')



def login(request) :

    errors = models.User.objects.login_validator(request.POST)
    
    
    if len(errors):
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        if request.method == "POST":
            Email = request.POST['Email']
            passwd = request.POST['passwd']
            user= models.get_user(Email)
            
            if user and bcrypt.checkpw(passwd.encode(), user.passwd.encode()):
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name 
                return redirect('/thoughts')
        return redirect('/')


def addthought(request):

    errors = models.Thought.objects.thoughts_validator(request.POST)
    
    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/thoughts')
    else:
       
        user_id = request.session['id']
    
        print(user_id)
        models.addthought(request.POST, user_id)

        return redirect('/thoughts')

def delete(request , id):

    models.delete(id)

    return redirect('/thoughts')



def thoughtid(request, id):

    context = {
        "this_thought":  models.get_thought_id(id),
        "all_users": models.get_all_users()
        

    }


    return render(request, "thoughts.html" ,context)

def like(request,id):
    user_id = request.session['id']
    models.like(user_id , id)

    return redirect('/thought/'+ str(id))


def unlike(request , id):
    user_id = request.session['id']
    models.unlike(user_id , id)

    return redirect('/thought/'+ str(id))

   

    


def logout(request):
    request.session.clear()
    return redirect("/")
