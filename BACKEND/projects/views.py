from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
# a view function is a func that takes a request and returns a response (request handler) 

from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer