from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
# a view function is a func that takes a request and returns a response (request handler) 

def calculate():
    x = 1
    y = 2
    return x

def proj(request):
    # we usually can pull from database
    # transform data
    # send somthing (emails, msgs...)
    calculate()
    return render(request, 'projects.html', {'name': 'proj1'})