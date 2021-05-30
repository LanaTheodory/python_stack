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
        if len(postData['fname']) < 2:
            errors["fname"] = "first name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last name should be at least 2 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "your password should be at least 8 characters"
        return errors
    def book_validator(self, postData):
        errors = {}
        if len(postData['description']) < 5:
            errors["description"] = "description should be at least 5 characters"
            return errors


class User(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE )
    users_who_like = models.ManyToManyField(User,related_name='liked_books')
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

    


# def get_user_cars(id):
#     user = User.objects.get(id=id)
#     return user.cars.all()

def check_password(passwd, conpasswd):
    # ok = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
    # okay = bcrypt.hashpw(conpasswd.encode(), bcrypt.gensalt()).decode()

    if passwd == conpasswd :

        return True

def addbook(postdata , id) : 
    return Book.objects.create(title = postdata['title'] ,
     description = postdata['description'] ,  uploaded_by = User.objects.get(id =id))

def addFavBook(user_id , book_id):
    this_user =  User.objects.get(id =user_id)
    this_book = Book.objects.get(id = book_id)
    x = this_user.liked_books.add(this_book)
    return x

def unfavorite(user_id , book_id):
    this_user =  User.objects.get(id =user_id)
    this_book = Book.objects.get(id = book_id)
    x = this_user.liked_books.remove(this_book)
    return x


def get_book():
    
    return Book.objects.all()


def get_all_users():
    
    return User.objects.all()


def get_book_id(id):
    return Book.objects.get(id=id)

def updatebook(data, id):
    c = Book.objects.get(id = id)
    if data['title']:
        c.title = data['title']
    if data['description']:
        c.description = data['description']
    c.save()

    return c

def deletebook(id):
    c = Book.objects.get(id = id)
    c.delete()
    return c
       




