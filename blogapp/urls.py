from django.urls import path
from . import views

# Create all urls here

urlpatterns = [
    path("",views.home,name='home'),

    path("register", views.register, name = 'register'),
    path("login", views.login , name = 'login'),

    path("create-blog", views.create_blog, name = 'create_blog'),
    path("blog-details/<int:id>", views.details_blog, name = 'details_blog'),
    path("update-blog/<int:id>", views.update_blog, name = 'updates_blog'),
    path("delete-blog/<int:id>", views.delete_blog, name = 'delete_blog'),
    
]
