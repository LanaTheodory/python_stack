from django.http import request
from django.shortcuts import redirect, render 
from . import models
from django.contrib import messages
import bcrypt
import re




def index(request):

    # review 

    if "id" in request.session:
        return redirect('/welcome')
    else:

        return render(request,"index.html")

def welcome(request):
    
    context ={
        'all_books' : models.get_book() ,
        "all_users" : models.get_all_users() ,
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
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name 
                return redirect('/welcome')
    return redirect('/')



def login(request) :
    if request.method == "POST":
        Email = request.POST['Email']
        passwd = request.POST['passwd']
        user= models.get_user(Email)
        print(user)
        if user and bcrypt.checkpw(passwd.encode(), user.passwd.encode()):
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name 
            return redirect('/welcome')
    return redirect('/')


def addbook(request):
    
    errors = models.Book.objects.book_validator(request.POST)
    if errors:
        if len(errors) > 0:

            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('/welcome')
        else:
            user_id = request.session['id']
            x = models.addbook(request.POST, user_id)
            book_id = x.id

            models.addFavBook(user_id ,book_id )


            return redirect('/welcome')
    return redirect('/welcome')
    

def bookdetails(request , id):
    context = {
        'this_book' : models.get_book_id(id),
        'this_user_id': request.session['id']
    }

    return render(request, 'bookdetails.html' , context)

def updatebook(request, id):
    errors = models.Book.objects.book_validator(request.POST)
   
    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/book/'+ str(id))
    else:

        models.updatebook(request.POST , id)

    return redirect('/welcome')

def deletebook(request, id):

    models.deletebook( id)
    return redirect('/welcome')

def unfavorite(request, id):
    user_id = request.session['id']
    models.unfavorite(user_id , id)
    return redirect('/book/'+ str(id))

def addfav(request, id):
    
    user_id = request.session['id']
    models.addFavBook(user_id , id)

    return redirect('/book/'+ str(id))


def logout(request):
    request.session.clear()
    return redirect("/")
