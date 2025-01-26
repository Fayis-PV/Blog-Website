from django.urls import path
from . import views
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# Create all urls here

urlpatterns = [
    path("", views.home, name='home'),

    path("register", views.register, name='register'),
    path("login", views.login_user, name='login'),
    path("logout", views.logout_user, name='logout'),

    path("create-blog", views.create_blog, name='create_blog'),
    path("blog-details/<int:id>", views.details_blog, name='details_blog'),
    path("update-blog/<int:id>", views.update_blog, name='update_blog'),
    path("delete-blog/<int:id>", views.delete_blog, name='delete_blog'),

    path('create-comment/<int:blog_id>', views.create_comment, name='create_comment'),

    path('approve-blog/<int:id>', views.approve_blog, name='approve-blog'),
    path('block-blog/<int:id>', views.block_blog, name='block-blog'),

    path('profile', views.profile, name = 'profile'),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='password_reset.html',
             html_email_template_name='password_reset_email.html' ),
         name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
