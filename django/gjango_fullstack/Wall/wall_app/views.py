from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from time import  strftime
# import bcrypt



def index(request):

    return render(request,"index.html")

 

def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    

    if len(errors) > 0:
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        print('start reg')
        if request.method == "POST" :
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            Email = request.POST['Email']
            passwd = request.POST['passwd']
            conpasswd = request.POST['conpasswd']

            
            if passwd == conpasswd  :
                
                print('passwords are confirmed')
                user = models.create_user(first_name ,last_name , Email , passwd)
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name 
                return redirect('/wall')
            

            # if models.check_password(passwd, conpasswd)  :
            #     hashed_passwd = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
            #     print('passwords are confirmed')
            #     user = models.create_user(first_name ,last_name , Email , hashed_passwd)
            #     request.session['id'] = user.id
            #     request.session['first_name'] = user.first_name
            #     request.session['last_name'] = user.last_name 
            #     return redirect('/wall')
    return redirect('/')

    
def main_wall(request):

    context = {
        "all_messages": models.get_message(),
        "all_comments": models.get_comment(),
        # "comment_id": models.comment_id(id),

    }

    return render(request, "main_wall.html", context)



def login(request) :
    if request.method == "POST":
        Email = request.POST['Email']
        passwd = request.POST['passwd']
        user= models.get_user(Email)
        print(user)
        if user and passwd ==  user.passwd:
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name 
            return redirect('/wall')
    return redirect('/')




###################################


def addmessage(request): 
    user_id = request.session['id'] 
    message = models.create_message(request.POST, user_id)
   # request.session['message_id']= message.id


    return redirect('/wall')


def addcomment(request):
    if request.method == 'POST':


        user_id = request.session['id'] 
        message_id = request.POST['message_id']
         

        models.create_comment(request.POST, user_id, message_id), 


        return redirect('/wall')
    return redirect('/wall')
    

#################################

def logout(request):
    request.session.clear()
    return redirect("/")

def delete(request):

    comment = models.get_comment()
    commenttime = comment.created_at
    seconds = commenttime.strftime('%M')
    

    if seconds < 30 :

        commentid = request.POST['comment_id'] 

        models.deletecomment(commentid)


    return redirect("/wall")
    




