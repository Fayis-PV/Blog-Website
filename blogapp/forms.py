from django import forms
from .models import *

# Create forms here

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","content","thumbnail"]
        