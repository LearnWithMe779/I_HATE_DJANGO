from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.

def Home(req:HttpRequest):
    return render(req,'home.html')