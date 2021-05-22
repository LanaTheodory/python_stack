from django.http.response import HttpResponse
from django.shortcuts import render, redirect,HttpResponse

def root(requests):
    return redirect("/blogs")


def index(requests):
    # return JsonResponse({"response":"placeholder to later display a list of all blogs", "status":True})
    return HttpResponse("placeholder to later display a list of all blogs")

def new(requests):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(requests):
    return redirect("/")

def show(requests, x):
    return HttpResponse (f"placeholder to display blog number: {x} ")

def edit(requests, x):
    return HttpResponse (f"placeholder to display blog number: {x} ")

def destroy (requests , x):
    return redirect("/blogs")
