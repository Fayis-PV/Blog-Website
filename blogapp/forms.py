from django import forms
from .models import *

# Create forms here

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','mobile','email','profile_pic']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","content","thumbnail"]
        