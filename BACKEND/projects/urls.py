from django.urls import path
from .views import ProjectListCreateView
from . import views

# url configuration

urlpatterns = [
    path('', ProjectListCreateView.as_view()),
]
