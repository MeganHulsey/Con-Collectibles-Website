from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return HttpResponse("<h1>Welcome to Con-Collectibles!</h1>")

def fruit1(response):
    return HttpResponse("Fruit 1!")

def fruit2(response):
    return HttpResponse("Fruit 2!")

def fruit3(response):
    return HttpResponse("Fruit 3!")
