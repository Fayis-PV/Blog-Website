from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='/img/profile/')
    mobile = models.IntegerField()

class Blog(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    BLOCKED = 'blocked'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (BLOCKED, 'Blocked'),
    ]

    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='/img/thumbnail')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=PENDING)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    commenter = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    notify = models.TextField()