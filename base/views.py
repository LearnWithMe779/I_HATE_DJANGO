from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.

rooms = [
        {'id':1,'name':'Python'},
        {'id':2,'name':"JS"}
]
def Home(req:HttpRequest):
    context = {"rooms":rooms}
    return render(req,'home.html',context=context)

def Room(req:HttpRequest,pk):
    room = None
    print(pk)
    for i in rooms:
        if(i['id'] == int(pk)):
            room = i 
    context = {'room':room}
    return render(req,'rooms.html',context=context)