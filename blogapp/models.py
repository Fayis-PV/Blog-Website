from django.db import models
from django.contrib.auth.models import AbstractUser, User

# # Create your models here.

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='img/profile/',null = True, blank = True)
    mobile = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return self.first_name +" "+ self.last_name

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
    thumbnail = models.ImageField(upload_to='img/thumbnail/')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=PENDING)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    commenter = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    notify = models.TextField()