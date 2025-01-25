from django.shortcuts import render
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):
    forms = RegisterForm()
    if request.method == 'POST':
        try:
            pass
        except:
            pass
    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        try:
            pass
        except:
            pass
    return render(request,"login.html")

def create_blog(request):
    pass

def details_blog(request,id):
    pass

def update_blog(request,id):
    pass

def delete_blog(request,id):
    pass

def create_command(request, blog_id):
    pass

