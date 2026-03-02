from django.urls import path
from . import views

# url configuration
urlpatterns = [
    path("pro/", views.do_something)
]