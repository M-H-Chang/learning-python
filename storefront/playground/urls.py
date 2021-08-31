from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# this is a URLConf ex
urlpatterns = [
    path('hello/', views.say_hello)
    # first param is the path of the function and the second one is a reference
    # since we are already in the playground directory Django knows which function to use
]
