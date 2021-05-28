from django.db import models
from django.shortcuts import redirect, render
from . import models

def index(request):

    return render(request, 'index.html')

def index2(request):
    if request.POST["forms"] == "register":
        x = models.create(request.POST)
        if x == True:
            request.session['email'] = request.POST['email']
            return redirect('/success')
        else:
             return redirect("/")


    if request.POST["forms"] == "login":

        email = request.POST["email1"]
        passwordd = request.POST["password1"]

        y = models.login(email , passwordd)
        
        if y == True:
            request.session['email'] = request.POST["email1"]
            return redirect('/success')

        
    return redirect("/")
        # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        # user= models.User.objects.filter(email = request.POST['email1'])
        # user1= request.POST['password1']
        # print(user)
        # print(user[0].password)
        # if user:
        #     print("hgtgtgtgjhgjugjk")
        #     if user1 == user[0].password:
        #         print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #         request.session['email'] = request.POST['email1']
        #         return redirect('/success')
        #     return redirect("/")
        # return redirect("/")

    # return redirect('/success')
    

        
        

       

    

def success(request):
    context = {
        "email" : request.session['email']

    }
    return render(request, 'success.html', context)

def logout(request):
    
    del request.session['email']
    return  redirect('/')
