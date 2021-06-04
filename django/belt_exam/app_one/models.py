from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.db import models
import bcrypt
import re



class BlogManager(models.Manager):
    def basic_validator(self, postData ):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(postData['Email']):    
            errors['Email'] = "Invalid email address!"
        unique=User.objects.filter(Email=postData['Email']).exists()
        if(unique):
            errors['unique'] = "Email exist!"
        if len(postData['fname']) < 2:
            errors["fname"] = "first name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last name should be at least 2 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "your password should be at least 8 characters"
        return errors
    def login_validator(self, postdata):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(postdata['Email']):    
            errors['Email'] = "Invalid email address!"
        if len(postdata['passwd']) < 8:
            errors["passwd"] = "your password should be at least 8 characters"
        return errors
    def thoughts_validator(self, data):
        errors = {}
        if len(data['description']) < 8:
            errors["description"] = "your description should be at least 8 characters"
        return errors



class User(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()

class Thought(models.Model) :
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="thoughts_uploaded", on_delete=models.CASCADE )
    users_who_like = models.ManyToManyField(User,related_name='liked_thoughts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()



def create_user(first_name , last_name , Email , passwd) : 
    
    
    return User.objects.create(first_name = first_name , last_name = last_name , Email = Email , passwd = passwd)


def get_user(Email):
    
    users=  User.objects.filter(Email=Email )
    if len(users)>0:
        return users[0]
    else:
        return None

    

def check_password(passwd, conpasswd):
  
    if passwd == conpasswd :

        return True

def get_all_users():
    
    return User.objects.all()

def addthought(postd, user_id):
    return Thought.objects.create(description = postd['description'] ,  uploaded_by = User.objects.get(id = user_id))

def get_all_thoughts():
    
    return Thought.objects.all()

def delete(id):
    c = Thought.objects.get(id = id)
    c.delete()
    return c

def like(user_id , thought_id):
    this_user =  User.objects.get(id =user_id)
    this_thought = Thought.objects.get(id = thought_id)
    x = this_user.liked_thoughts.add( this_thought)
    return x

def unlike(user_id , thought_id):
    this_user =  User.objects.get(id =user_id)
    this_thought = Thought.objects.get(id = thought_id)
    x = this_user.liked_thoughts.remove( this_thought)
    return x

def get_thought_id(id):
    return Thought.objects.get(id=id)


