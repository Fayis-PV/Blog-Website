from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-timestamp').values()
    return render(request, 'index.html',{'blogs':blogs})


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
                custom = CustomUser(first_name= first_name, last_name = last_name,username = username, email = email)
                custom.set_password(password)
                custom.save()
                messages.success(request, 'User Created Successfully')
                return redirect('login')
        except Exception as e:
            messages.error(request,str(e))
            
    return render(request,"register.html")
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            # print(CustomUser.objects.all())
            print(username)
            user = CustomUser.objects.get(username = username)
            status = user.check_password(password)
            if user :
                authenticate(request, username = username, password = password)
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,'Invalid Credentials')
        except Exception as e:
            messages.error(request,'Error'+str(e))
            
    return render(request,"login.html")

@login_required(login_url='/login')
def create_blog(request):
    form = BlogForm()
    if request.user:
        
        print(request.FILES)
        if request.method == 'POST':
            form = BlogForm(request.POST,request.FILES)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = request.user
                blog.save()
                messages.success(request,'Successfully added new blog')
                return redirect('/')
            else:
                messages.error(request,'Please clearly fill all forms')
    else:
        return redirect('/login')
    return render(request,'create_blog.html',{'form':form})

@login_required(login_url='/login')
def details_blog(request,id):
    if request.user:
        print(request.user)
        blog= Blog.objects.get(id = id)
        if blog:
            return render(request, 'article.html',{'blog':blog, 'user':request.user})
        messages.error(request,'Error occured:'+str())
        return redirect('/')
    return redirect('/login')

@login_required(login_url='/login')
def update_blog(request,id):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = Blog.objects.get(id=id)
            blog.title = form.cleaned_data.get('title')
            blog.content = form.cleaned_data.get('content')
            blog.thumbnail = form.cleaned_data.get('thumbnail')
            blog.save()
            messages.success(request, 'Successfully updated the blog')
            return redirect('/')
        else:
            messages.error(request, 'Please clearly fill all forms')
    else:
        return redirect('/login')
    return render(request, 'create_blog.html', {'form': form})

@login_required(login_url='/login')
def delete_blog(request,id):
    try:
        blog = Blog.objects.get(id = id)
        blog.delete()
        messages.success(request,'The blog deleted successfully')
        return redirect('/')
    except Exception as e:
        messages.error(request,'An Error Occured:'+str(e))

@login_required(login_url='/login')
def create_command(request, blog_id):
    if request.method == 'POST':
        try:
            blog = Blog.objects.get(pk = blog_id)
            comment = request.POST['comment']
            blog.comment_set.create(comment =comment,commenter = request.user)
            messages.success(request,'Comment added')
            return redirect(f'/details/{blog_id}')
        except Exception as e:
            messages.error(request, 'Error Occurred: '+str(e))
    return redirect('/')
