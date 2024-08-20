from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "caboodle/base.html", {})

def home(response):
    return render(response, "caboodle/home.html", {})

#def fruit1(response):
    #return HttpResponse("Fruit 1!")

#def fruit2(response):
    #return HttpResponse("Fruit 2!")

#def fruit3(response):
    #return HttpResponse("Fruit 3!")
