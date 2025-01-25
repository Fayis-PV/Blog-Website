from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        try:
            if password != cpassword and password != '':
                messages.error(request, 'Password doesn\'t match')
            elif CustomUser.objects.filter(email = email):
                messages.error(request, 'User with same email already exists')
            else:
                messages.success(request, 'User Created Successfully')
                custom = CustomUser(first_name= first_name, last_name = last_name,username = username, email = email, password = password)
                custom.save()
                return redirect('login')
        except Exception as e:
            messages.error(request,str(e))
            
    return render(request,"register.html")
    


def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.filter(email = email, password = password)
            authenticate(request, email = email, password = password)
        except Exception as e:
            messages.error(request,e)
            
    return render(request,"login.html")

def create_blog(request):
    form = BlogForm()
    if request.user:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = request.user
                blog.save()
                messages.success(request,'Successfully added new blog')
                return redirect('/')
            else:
                messages.error(request,'Please clearly fill all forms')
    return render(request,'create_blog.html',{'form':form})

def details_blog(request,id):
    pass

def update_blog(request,id):
    if request.method == 'POST':
        try:
            pass
        except:
            pass
    return render(request,"login.html")

def delete_blog(request,id):
    if request.method == 'POST':
        try:
            pass
        except:
            pass
    return render(request,"login.html")

def create_command(request, blog_id):
    if request.method == 'POST':
        try:
            pass
        except:
            pass
    return render(request,"login.html")

