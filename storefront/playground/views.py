from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> respones
# request handler
# action
# not like other views, it does not return a view. In python it is called a template


def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Min'})
