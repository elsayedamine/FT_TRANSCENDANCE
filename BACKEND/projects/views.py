from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
# a view function is a func that takes a request and returns a response (request handler) 

def do_something(request):
    # we usually can pull from database
    # transform data
    # send somthing (emails, msgs...)
    return HttpResponse("hello world")